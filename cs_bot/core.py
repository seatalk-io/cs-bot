"""
Copyright 2022 SeaTalk Open Platform

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import signal
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from types import FrameType
from typing import Optional, Any, Dict, List, Union

import jwt
from flask import Flask, request
from jwt import DecodeError
from pydantic import ValidationError

from cs_bot.libs.seatalk_webhook.client import WebhookMsgType, WebhookClient
from cs_bot.session import FSM
from cs_bot.metrics import report_message_handled, Status
from cs_bot.store import CacheManager, Storage
from cs_bot.plugin import Plugin, PluginManager, filter_matchers, PluginAPI
from cs_bot.session import MessageSession, SessionManager
from cs_bot.hooks.matcher import Matcher
from cs_bot.hooks.bot_lifecycle import BotLifecycle
from cs_bot.scheduler import Scheduler
from cs_bot.adapter import BaseAdapter
from cs_bot.api_common import standard_response, plugin_api_internal_error, plugin_api_not_found, plugin_not_found, \
    plugin_config_invalid, plugin_not_enabled, APIAuth, plugin_api_no_permission, AuthUser, plugin_api_auth_required
from cs_bot.configs.startup_config import StartupConfig, DEFAULT_STARTUP_CONFIG
from cs_bot.log import logger
from cs_bot.protocol import CallbackMessage, EventType, Message, EventChatMessage
from cs_bot.typing import EventHandler_F, State_T


class BaseBot:
    def __init__(self, config: Optional[StartupConfig] = None):
        if config is None:
            config = DEFAULT_STARTUP_CONFIG
        self.config: StartupConfig = config
        self.debug: bool = config.debug
        self.adapter: Optional[BaseAdapter] = None

        self.event_handler: Optional[EventHandler_F] = None
        # Workers
        self._setup_signal_trap()
        self._message_handler_pool: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=config.max_msg_handler_workers)
        # API
        self._app: Flask = Flask(__name__)
        self._setup_web_server()

    def register_adapter(self, adapter: BaseAdapter):
        self.adapter = adapter

    def get_app(self):
        return self._app

    def on_event(self):
        def decorator(f: EventHandler_F) -> EventHandler_F:
            self.event_handler = f
            return f

        return decorator

    def _check_run_requirements(self):
        if self.adapter is None:
            self._stop()
            raise ValueError("adapter is None, use cs_bot.register_adapter(adapter: Adapter) "
                             "to set a register before the cs_bot.run()")

    def run(self, host: str, port: int):
        """
        Runs the application on a local development server.
        :return: None
        """
        self._check_run_requirements()
        self._app.run(host, port)

    def _setup_web_server(self):
        self._setup_event_api()

    def _setup_event_api(self):
        @self._app.post(self.config.callback_path)
        def receive_message() -> Any:
            headers = {k: request.headers.get(k, type=str) for k in request.headers.keys()}
            raw_body = request.data
            response: Any = self.adapter.get_response(raw_body, headers)
            self._message_handler_pool.submit(self._handle_event, raw_body=raw_body, headers=headers)
            return response or standard_response()

    def _handle_event(self, raw_body: bytes, headers: Dict[str, str]):
        event: Optional[CallbackMessage] = None
        if self.event_handler is not None:
            try:
                event = self.adapter.extract_event(raw_body, headers)
            except Exception as e:
                logger.error(f"Adapter.extract_event error {traceback.format_exc()}")

            if event is None:
                logger.warning(f"Adapter.extract_event produce none event")
                return

            try:
                self.event_handler(event)
            except Exception as e:
                logger.error(f"event_handle produced an error {traceback.format_exc()}")
        else:
            logger.warning("event_handler is not registered")

    def _setup_signal_trap(self):
        signal.signal(signal.SIGINT, self._signal_trap)

    def _signal_trap(self, signal_num: signal.Signals, frame: FrameType):
        self._stop()
        exit(0)

    def _stop(self):
        self._message_handler_pool.shutdown(wait=False)


class CSBot(BaseBot):
    def __init__(self, config: Optional[StartupConfig] = DEFAULT_STARTUP_CONFIG):
        super().__init__(config)

        self._webhook_client: WebhookClient = WebhookClient(config.webhooks)

        self._lifecycle: BotLifecycle = BotLifecycle()
        self.plugin_manager: PluginManager = PluginManager()

        self.background_task_pool: ThreadPoolExecutor = ThreadPoolExecutor(
            max_workers=8
        )
        self._scheduler_running: bool = False
        self._scheduler_stopping: bool = False

        self._schedule = Scheduler()
        self._start_scheduler_loop()

        self.cache: CacheManager = CacheManager(self.config.redis)
        self.store: Storage = Storage()
        self.store.init(config.db)
        self.fsm_mapping: Dict[Union[str, State_T], FSM] = {}

        self._session_manager = SessionManager(self.cache)

        self._setup_startup_hooks()
        self._extend_web_server()
        self._setup_event_handler()

        self._lifecycle.emit_startup()

    def on_event(self):
        if self.event_handler is None:
            return super(CSBot, self).on_event()
        return None

    @property
    def lifecycle(self) -> BotLifecycle:
        return self._lifecycle

    @property
    def scheduler(self) -> Scheduler:
        return self._schedule

    def send(self, receiver_email: Union[str, List[str]], message: Union[str, Message]):
        if isinstance(message, str):
            message = Message(content=message)
        if isinstance(receiver_email, str):
            receiver_email = [receiver_email]
        for receiver in receiver_email:
            self.adapter.send(receiver, message)

    def send_group(self, group_name: str, message: Union[str, Message], mentioned_emails: Optional[List[str]] = None):
        if isinstance(message, str):
            message = Message(content=message)
        return self.adapter.send_group(group_name, message, mentioned_emails)

    def reply(self, event: EventChatMessage, message: Union[str, Message], quote_reply: bool = False):
        if isinstance(message, str):
            message = Message(content=message)
        return self.adapter.reply(event, message, quote_reply)

    def register_fsm(self, fsm_name: str, state_class: State_T) -> FSM:
        if fsm_name in self.fsm_mapping:
            raise ValueError(f"FSM with name of [{fsm_name}] has already been registered.")
        if state_class in self.fsm_mapping:
            raise ValueError(f"FSM with State_T of [{state_class}] has already been registered.")
        new_fsm = FSM(self, fsm_name, state_class)
        self.fsm_mapping[fsm_name] = new_fsm
        self.fsm_mapping[state_class] = new_fsm
        return new_fsm

    def get_fsm(self, key: Union[str, State_T]) -> FSM:
        fsm = self.fsm_mapping.get(key, None)
        if fsm is not None:
            return fsm
        raise ValueError(f"FSM [{key}] is not registered yet.")

    def webhook(self, message: Union[str, bytes], msg_type: WebhookMsgType = WebhookMsgType.TEXT):
        self._webhook_client.send(message, msg_type)

    def _start_scheduler_loop(self):
        if self._scheduler_running:
            return
        self._scheduler_running = True
        self.background_task_pool.submit(self._scheduler_loop)

    def _scheduler_loop(self):
        while True:
            if self._scheduler_stopping:
                break
            try:
                self._schedule.run_pending()
            except Exception as e:
                logger.error("failed to execute pending schedulers, err: %s", e)
            time.sleep(1)

    def _setup_startup_hooks(self):
        @self.get_app().before_first_request
        def background_startup():
            threading.Thread(target=self.lifecycle.emit_startup).start()

    def _extend_web_server(self):
        self._setup_open_api()
        self._setup_admin_api()
        self._setup_plugin_api()

    def _setup_event_handler(self):
        @self.on_event()
        def event_handler(event: CallbackMessage):
            start = time.time()
            if event.event_type == EventType.NEW_CHAT_MESSAGE:
                sess: MessageSession = MessageSession(self, event, self._session_manager)
                matchers: List[Matcher] = filter_matchers(sess)
                if not matchers:
                    report_message_handled(Status.NO_MATCH, time.time() - start)
                    return
                try:
                    for matcher in matchers:
                        matcher.process(sess)
                        if sess.aborted:
                            break
                    status = Status.OK if sess.reply_count > 0 else Status.NO_REPLY
                    report_message_handled(status, time.time() - start)
                except Exception as e:
                    logger.error("failed to process the message, err: %s\n%s", e, traceback.format_exc())
                    report_message_handled(Status.ERROR, time.time() - start)
            elif event.event_type == EventType.NEW_SUBSCRIBER:
                pass

    def _setup_open_api(self):
        pass

    def _setup_admin_api(self):
        @self._app.get("/admin/plugins/list")
        def plugin_list():
            return {"plugins": list(map(lambda plugin: plugin.to_json(), PluginManager.plugins.values()))}

        @self._app.post("/admin/plugins/status/<plugin_name>")
        def update_plugin_status(plugin_name: str):
            plugin: Optional[Plugin] = self.plugin_manager.get_plugin_by_name(plugin_name)
            if plugin is None:
                return plugin_not_found(plugin_name)
            plugin.enabled = request.json.get("enabled")
            return standard_response()

        @self._app.post("/admin/plugins/update_config/<plugin_name>")
        def update_plugin_config(plugin_name: str):
            plugin: Optional[Plugin] = self.plugin_manager.get_plugin_by_name(plugin_name)
            if plugin is None:
                return plugin_not_found(plugin_name)
            try:
                plugin.update_config(request.json)
                return standard_response()
            except ValidationError as e:
                return plugin_config_invalid(e.errors())

        @self._app.get("/admin/plugins/get_config/<plugin_name>")
        def get_plugin_config(plugin_name: str):
            plugin: Optional[Plugin] = self.plugin_manager.get_plugin_by_name(plugin_name)
            if plugin is None:
                return plugin_not_found(plugin_name)
            try:
                return standard_response(data=plugin.config.dict())
            except Exception as e:
                return standard_response(data={})

        @self._app.get("/admin/plugins/get_config_schema/<plugin_name>")
        def get_config_schema(plugin_name: str):
            plugin: Optional[Plugin] = self.plugin_manager.get_plugin_by_name(plugin_name)
            if plugin is None:
                return plugin_not_found(plugin_name)
            if plugin.config_class is not None:
                return standard_response(data=plugin.config_class.schema())

    def _setup_plugin_api(self):
        @self._app.route("/plugins/<plugin_name>/<api_path>")
        def plugin_custom_api(plugin_name: str, api_path: str) -> Any:
            return self._handle_plugin_api(plugin_name, api_path)

    def _handle_plugin_api(self, plugin_name: str, api_path: str):
        the_plugin: Optional[Plugin] = self.plugin_manager.get_plugin_by_name(plugin_name)
        if the_plugin is None:
            return plugin_not_found(plugin_name)
        if not the_plugin.enabled:
            return plugin_not_enabled(plugin_name)

        api: Optional[PluginAPI] = the_plugin.get_api_handler(api_path, request.method)
        if api is None:
            return plugin_api_not_found(plugin_name, api_path, request.method)

        auth_user: AuthUser = AuthUser(False, None, APIAuth.Anonymous)
        if api.auth_role.value > APIAuth.Anonymous.value:
            incoming_jwt = request.headers.get("authorization", None)
            if incoming_jwt is None:
                return plugin_api_auth_required(plugin_name, api_path, request.method)
            try:
                payload = jwt.decode(incoming_jwt, self.config.jwt_secret, algorithms=["HS256"])
                role = payload.get("role", 0)
                if role < api.auth_role.value:
                    return plugin_api_no_permission(plugin_name, api_path, request.method, api.auth_role)
                auth_user.is_authenticated = True
                auth_user.role = APIAuth(role)
                auth_user.user = payload.get("email")
            except DecodeError as e:
                logger.warning("decode jwt failed, jwt: %s, err: %s", incoming_jwt, e)
                return
            except Exception as e:
                if self.debug:
                    return plugin_api_internal_error(traceback.format_exc())
                return plugin_api_internal_error("")
        try:
            return api.handler()
        except Exception as e:
            if self.debug:
                return plugin_api_internal_error(traceback.format_exc())
            return plugin_api_internal_error("")

    def _stop(self):
        self._scheduler_stopping = True
        self._message_handler_pool.shutdown(wait=False)
        self.background_task_pool.shutdown(wait=True)
        self._scheduler_running = False
