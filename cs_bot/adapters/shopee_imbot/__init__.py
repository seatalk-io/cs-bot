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
import base64
import json
from typing import Dict, Any, Optional, List
import msgpack
import requests
from pydantic import BaseModel
from requests import Response

from cs_bot import BaseAdapter, logger
from cs_bot.protocol import Message, CallbackMessage, EventType, MsgType, EventChatMessage, ChannelType, UserInfo, \
    QuoteMessage


class ReceiveNewMessageRequest(BaseModel):
    """
    OnMessage callback request definition,
    used to deserialize the callback requests from the shopee_imbot callback server
    """
    sender_name: str
    channel_type: str
    sender_email: str
    content: str
    raw: str
    msg_type: MsgType
    quote: Optional[Dict]
    msg_id: str = ""


class Adapter(BaseAdapter):
    """
    Adapter implement to adapt the shopee_imbot callback server
    """
    CMD_GROUP = 769
    CMD_PERSON = 513
    CallbackTemplate: Dict[EventType, BaseModel] = {
        "on_msg": ReceiveNewMessageRequest
    }

    def __init__(self, bot: 'CSBot', config: Dict[str, Any]):
        super().__init__(bot, config)
        self.bot = bot
        self.host: str = config["host"]

    def get_response(self, raw_body: bytes, headers: Dict[str, str]) -> Any:
        return None

    def extract_event(self, raw_body: bytes, headers: Dict[str, str]) -> Optional[CallbackMessage]:
        """
        shopee-imbot has only one EventType: EventType.NEW_CHAT_MESSAGE
        :param raw_body:
        :param headers:
        :return:
        """
        request = ReceiveNewMessageRequest(**json.loads(raw_body))
        raw = msgpack.loads(base64.b64decode(request.raw))
        msg_content = request.content
        if request.msg_type in {MsgType.IMAGE, MsgType.STICKER_C}:
            msg_content = base64.b64decode(msg_content)
        chat_event = EventChatMessage(
            id=request.msg_id,
            sender=UserInfo(
                name=request.sender_name,
                email=request.sender_email
            ),
            message=Message(
                content=msg_content,
                msg_type=MsgType(request.msg_type),
                channel_type=ChannelType(request.channel_type)
            ),
            channel_type=ChannelType(request.channel_type),
            raw=raw,
        )
        if request.quote is not None:
            chat_event.quoted_message = QuoteMessage(
                message=Message(
                    content=request.quote.get("text"),
                    msg_type=MsgType.TEXT,
                    channel_type=ChannelType(request.channel_type)
                ),
                sender=UserInfo(
                    name=request.quote.get("sender_name"),
                    email=request.quote.get("sender_email")
                )
            )
        return CallbackMessage(
            event_type=EventType.NEW_CHAT_MESSAGE,
            event=chat_event
        )

    def send(self, receiver_email: str, message: Message):
        res = requests.post(self.host + "/send", json={
            "content": self.encoded_content(message),
            "u_name": receiver_email,
            "msg_type": str(message.msg_type.value),
            "g_name": ""
        })
        if res.status_code != 200:
            raise ValueError(f"send message failed [{res.status_code} {res.text}]")

    @staticmethod
    def encoded_content(message: Message):
        if isinstance(message.content, bytes):
            return base64.b64encode(message.content).decode()
        return message.content

    def send_group(self, group_name: str, message: Message, mentioned_emails: Optional[List[str]] = None):
        if mentioned_emails is None:
            mentioned_emails = []
        res = requests.post(self.host + "/send", json={
            "content": self.encoded_content(message),
            "u_name": ",".join(mentioned_emails),
            "msg_type": str(message.msg_type.value),
            "g_name": group_name
        })
        if res.status_code != 200:
            raise ValueError(f"send group message failed [{res.status_code} {res.text}]")

    def reply(self, event: EventChatMessage, message: Message, quote_reply: bool = False):
        cmd = self.CMD_PERSON
        if event.group is not None:
            cmd = self.CMD_GROUP
        res = requests.post(self.host + "/quote_reply", json={
            "text": self.encoded_content(message),
            "cmd": cmd,
            "raw": base64.b64encode(msgpack.dumps(event.raw)).decode(),
            "quote_reply": quote_reply
        })
        if res.status_code != 200:
            raise ValueError(f"reply message failed [{res.status_code} {res.text}]")
