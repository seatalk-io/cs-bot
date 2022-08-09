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

from typing import Optional, List, Union
from flask import Flask

from cs_bot.configs.startup_config import StartupConfig
from cs_bot.session import FSM
from cs_bot.log import logger
from cs_bot.adapter import BaseAdapter
from cs_bot.api_common import plugin_api_internal_error, plugin_api_not_found, plugin_not_found, APIAuth
from cs_bot.configs.startup_config import StartupConfig, DEFAULT_STARTUP_CONFIG
from cs_bot.core import BaseBot, CSBot
from cs_bot.hooks.bot_lifecycle import BotLifecycle
from cs_bot.hooks.matcher import Matcher
from cs_bot.permissions import Permission
from cs_bot.plugin import PluginManager, Plugin, filter_matchers
from cs_bot.protocol import CallbackMessage, EventType, Message
from cs_bot.scheduler import Scheduler, Job
from cs_bot.session import MessageSession
from cs_bot.store import CacheManager, Storage
from cs_bot.typing import PluginAPI_F, Adapter_T, MessageProcessorHook_D, MessageProcessor, PluginLoadedHook_D, \
    PluginLoadedHook_F, PluginUnloadHook_D, PluginConfigUpdateHook_D, Words_T, PluginAPI_D, AutoUpdateConfig_D, \
    PluginConfig_T, Export_D, Export_F, State_T, LifecycleHook_D

_bot: Optional[CSBot] = None


def get_bot() -> CSBot:
    """
    get the global CSBot instance
    :return: _bot: CSBot
    """
    if _bot is None:
        raise ValueError("cs_bot has not been initialized, call cs_bot.init() first.")
    return _bot


def get_app() -> Flask:
    """
    get the Flask wsgi app
    :return: Flask instance
    """
    return get_bot().get_app()


def run(host: str = "0.0.0.0", port: int = "1127"):
    """
    Runs the application on a local development server
    :param host: the hostname to listen on. Set this to ``'0.0.0.0'`` to have the server available externally as well. Defaults to ``'127.0.0.1'``
    :param port: the port of the webserver. Defaults to ``5000`` or the
           port defined in the ``SERVER_NAME`` config variable if present.
    :return:
    """
    get_bot().run(host, port)


def load_plugin(module_path: str):
    """
    Load a python module as a plugin.
    :param module_path: path of the python module
    :return: None
    """
    return _load_plugin(module_path)


def load_plugins(module_path_list: List[str]):
    for module_path in module_path_list:
        _load_plugin(module_path)


def load_build_in_plugins():
    pass


def _load_plugin(module_path: str):
    return get_bot().plugin_manager.load_plugin(module_path)


def init(config: Optional[StartupConfig] = None):
    """
    Initialize the global default CSBot instance
    :param config: StartUpConfig. See details in the documentation Advanced -> StartUpConfig
    :return: None
    """
    global _bot
    if _bot is None:
        _bot = CSBot(config)


def register_adapter(adapter_class):
    """
    Declare which adapter is supposed to use.
    :param adapter_class: an implementation class of the abstract class cs_bot.adapter.Adapter
    :return: None
    """
    assert issubclass(adapter_class, BaseAdapter)
    bot = get_bot()
    return bot.register_adapter(adapter_class(bot, bot.config.adapter))


# message
def send(receiver_email: Union[str, List[str]], message: Union[str, Message]):
    """
    Send message to bot subscribers. batch send is support
    :param receiver_email: a string or a list of string to indicate the receivers' emails
    :param message:
    :return:
    """
    return get_bot().send(receiver_email, message)


def send_group(group_name: str, message: Union[str, Message], mentioned_emails: Optional[List[str]] = None):
    return get_bot().send_group(group_name, message, mentioned_emails)


# matchers
def on_prefix(prefix: Words_T, permission: Optional[Permission] = None, priority: int = 0) -> MessageProcessorHook_D:
    """
    Register a message handle function to match the text messages with a prefix of the given `prefix: Words_T`
    :param prefix: a string or a list of string to indicate the prefixes to match
    :param permission: a rule to tell which subscriber can trigger this message handler
    :param priority: determine the order of the message handlers
    :return: the decorator used to register the message handler
    """
    return PluginManager.on_prefix(prefix, permission, priority)


def on_regex(pattern: Words_T, permission: Optional[Permission] = None, priority: int = 0) -> MessageProcessorHook_D:
    """
    Register a message handle function to handle the text messages
    who match at least one of the given regular expressions
    :param pattern: a regular expression str or a list of regular expression str to indicate the prefixes to match
    :param permission: a rule to tell which subscriber can trigger this message handler
    :param priority: determine the order of the message handlers
    :return: the decorator used to register the message handler
    """
    return PluginManager.on_regex(pattern, permission, priority)


def on_keyword(keyword: Words_T, permission: Optional[Permission] = None, priority: int = 0) -> MessageProcessorHook_D:
    """
    Register a message handle function to handle the text messages who contain at least one of the given keywords
    :param keyword: a keyword str or a list of keyword str to indicate the prefixes to match
    :param permission: a rule to tell which subscriber can trigger this message handler.
    :param priority: determine the order of the message handlers.
    :return: the decorator used to register the message handler.
    """
    return PluginManager.on_keyword(keyword, permission, priority)


def on_exact(keyword: Words_T, permission: Optional[Permission] = None, priority: int = 0) -> MessageProcessorHook_D:
    """
    Register a message handle function to handle the text messages who exactly match at least one of the given keywords
    :param keyword: a keyword str or a list of keyword str to indicate the prefixes to match
    :param permission: a rule to tell which subscriber can trigger this message handler
    :param priority: determine the order of the message handlers
    :return: the decorator used to register the message handler
    """
    return PluginManager.on_exact(keyword, permission, priority)


def on_image(permission: Optional[Permission] = None, priority: int = 0) -> MessageProcessorHook_D:
    """
    Register a message handle function to handle the image/sticker messages
    :param permission: a rule to tell which subscriber can trigger this message handler
    :param priority: determine the order of the message handlers
    :return:
    """
    return PluginManager.on_image(permission, priority)


def on_any(permission: Optional[Permission] = None, priority: int = 0):
    return PluginManager.on_any(permission, priority)


# bot hooks
def on_start_up() -> LifecycleHook_D:
    """
    register a hook which will be called after the bot app is initialized
    :return: a decorator to register the hook function
    """
    return get_bot().lifecycle.on_startup()


# plugin hooks
def on_plugin_loaded() -> PluginLoadedHook_D:
    """
    This function should be called in a plugin.
    It returns a decorator which is used to register a hook called after the current plugin is loaded.
    :return: PluginLoadedHook_D
    """
    return PluginManager.on_plugin_loaded()


def on_plugin_unload() -> PluginUnloadHook_D:
    """
   This function should be called in a plugin.
   It returns a decorator which is used to register a hook called after the current plugin is unloaded.
   :return: PluginLoadedHook_D
   """
    return PluginManager.on_plugin_unloaded()


def on_config_updated(immediate: bool = False) -> PluginConfigUpdateHook_D:
    """
   This function should be called in a plugin.
   It returns a decorator which is used to register a hook called after the current plugin is loaded.
   :return: PluginLoadedHook_D
   """
    return PluginManager.on_config_updated(immediate)


def export_func(alias: Optional[str] = None) -> Export_D:
    return PluginManager.export(alias)


def register_fsm(fsm_name: str, state_class: State_T) -> FSM:
    """
    Register a state and create a fsm instance.
    The fsm instance maintains the states for the every user at the background
    :param fsm_name: a string to identify the FSM instance
    :param state_class: the user defined states
    :return: the created FSM instance
    """
    return get_bot().register_fsm(fsm_name, state_class)


def import_func(plugin_name: str, function_name: str) -> Optional[Export_F]:
    p = PluginManager.get_plugin_by_name(plugin_name)
    return None if p is None else p.get_exported_func(function_name)


# plugin API
def register_plugin_api(path: str, methods: List[str], auth_role: APIAuth = APIAuth.Anonymous) -> PluginAPI_D:
    return PluginManager.register_plugin_api(path, methods)


# schedulers
def every(interval: int) -> Job:
    """
    Schedule a new periodic job
    :param interval: A quantity of a certain time unit
    :return: An un-configured :class:`Job <Job>`
    """
    return get_bot().scheduler.every(interval)


def cancel_job(job: Job):
    """
    Delete a scheduled job
    :param job: The job to be unscheduled
    """
    return get_bot().scheduler.cancel_job(job)


def cache() -> CacheManager:
    return get_bot().cache


def store() -> Storage:
    return get_bot().store


def get_config(plugin_name: str) -> PluginConfig_T:
    return get_bot().plugin_manager.get_config(plugin_name)
