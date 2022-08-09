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
import hashlib
from typing import Dict, Any, Tuple, Optional, List

from cs_bot import BaseAdapter, Message
from cs_bot.log import logger
from cs_bot import protocol
from cs_bot.adapters.sop_bot.events import CallbackRequest, EventType
from cs_bot.libs.seatalk_openapi.client import SeaTalkOpenAPIClient
from cs_bot.protocol import UserInfo


class Adapter(BaseAdapter):
    _name = "sop_bot.Adapter"

    def __init__(self, bot: 'CSBot', config: Dict[str, Any]):
        """
        Initialize the SOP Bot Adapter
        :param bot: CSBot instance
        :param config: StartupConfig.adapter
        """
        super().__init__(bot, config)
        self.bot = bot
        self._app_id: str = config.get("app_id", "")
        self._app_secret: str = config.get("app_secret", "")
        if self._app_id == "" or self._app_secret == "":
            logger.warning(f"[{self._name}] app_id and app_secret should not be empty")
        self._signing_secret: bytes = config.get("signing_secret", "").encode("latin-1")
        if self._signing_secret == "":
            logger.warning(f"[{self._name}] signing_secret should not be empty")
        self.openapi: SeaTalkOpenAPIClient = SeaTalkOpenAPIClient(self._app_id, self._app_secret)

    def get_response(self, raw_body: bytes, headers: Dict[str, str]) -> Any:
        """
        :return: HTTP Response to return
        """
        try:
            request: CallbackRequest = CallbackRequest.parse_raw(raw_body)
            if request.event_type == EventType.VERIFICATION:
                return request.event.dict()
        except Exception:
            return None
        return None

    def extract_event(self, raw_body: bytes, headers: Dict[str, str]) -> Optional[protocol.CallbackMessage]:
        """
        https://open.seatalk.io/docs/messaging_messaging-events
        extract event from the callback request of the Seatalk Open Platform.
        :param raw_body: http body
        :param headers: http headers
        :rtype: protocol.CallbackMessage
        """
        request: CallbackRequest = CallbackRequest.parse_raw(raw_body)
        signature: str = headers.get("Signature", "")
        calculated = hashlib.sha256(raw_body + self._signing_secret).hexdigest()
        logger.info(f"[{self._name}] calculated signature {calculated} signature: {signature}")
        event_type = request.event_type
        if event_type == EventType.SINGLE_CHAT:
            employee_code = request.event.employee_code
            user_info = self.get_user_info([employee_code]).get(employee_code, None)
            if user_info is None:
                logger.warning(
                    f"[{self._name}] employee_code {employee_code} is not available with the current data scope"
                )
                return None
            return protocol.CallbackMessage(
                event_type=protocol.EventType.NEW_CHAT_MESSAGE,
                event=protocol.EventChatMessage(
                    id=request.event_id,
                    sender=user_info,
                    message=protocol.Message(
                        content=request.event.message.text.content,
                        msg_type=protocol.MsgType.TEXT,
                        channel_type=protocol.ChannelType.PRIVATE
                    ),
                    channel_type=protocol.ChannelType.PRIVATE,
                    raw=request.dict()
                )
            )
        elif event_type == EventType.NEW_SUBSCRIBER:
            employee_code = request.event.employee_code
            user_info = self.get_user_info([employee_code]).get(employee_code, None)
            if user_info is None:
                return None
            return protocol.CallbackMessage(
                event_type=protocol.EventType.NEW_SUBSCRIBER,
                event=protocol.EventNewSubscriber(
                    new_friends=user_info
                )
            )
        return None

    def get_user_info(self, employee_codes: List[str]) -> Dict[str, protocol.UserInfo]:
        """
        get UserInfo by the employee_code
        :param employee_codes: employee_code of the Seatalk Open Platform
        :return: the respective user info
        """
        return dict(map(
            lambda e: (e.employee_code, UserInfo(email=e.email, name=e.name)),
            self.openapi.get_contact_profile_v2(employee_codes).employees
        ))

    def send(self, receiver_email: str, message: protocol.Message):
        """
        let the bot send a message
        :param receiver_email: email
        :param message: Message Instance
        :return: None
        :raise: raise ValueError on invalid input message
        """
        result = self.openapi.get_employee_code_with_email(emails=[receiver_email])
        employee_code: Optional[str] = result.get(receiver_email, None)
        if employee_code is None:
            err = f"[{self._name}] email {receiver_email} is not available with the current data scope"
            logger.warning(err)
            raise ValueError(err)
        self.openapi.send_single_chat_message(employee_code, message.content, message.msg_type.value)

    def reply(self, event: protocol.CallbackMessage, message: protocol.Message, quote_reply: bool = False):
        """
        Let the bot reply a message
        :param quote_reply: whether to quote the incoming message, not supported yet
        :param event: the origin event to reply
        :param message: the reply
        :return: None
        :raise: raise ValueError on invalid input message
        """
        if quote_reply:
            logger.warning("[%s] quote_reply is not supported yet", self._name)
        return self.send(event.event.sender.email, message)

    def send_group(self, group_name: str, message: Message, mentioned_emails: Optional[List[str]] = None):
        raise NotImplementedError()
