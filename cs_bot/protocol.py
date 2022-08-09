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
from enum import Enum
from typing import Union, List, Dict, Any, Optional

from pydantic import BaseModel


# Event Type
class EventType(Enum):
    NEW_CHAT_MESSAGE = "new_chat_message"
    NEW_SUBSCRIBER = "new_subscriber"


# Adapter
class MsgType(Enum):
    TEXT = "text"
    IMAGE = "image"
    MARKDOWN = "markdown"
    STICKER_C = "sticker.c"


class ChannelType(Enum):
    GROUP = "group"
    PRIVATE = "private"


class UserInfo(BaseModel):
    name: str
    email: str


class GroupInfo(BaseModel):
    group_name: str
    group_code: str


class Message(BaseModel):
    content: Union[str, bytes]
    msg_type: MsgType = MsgType.TEXT
    channel_type: ChannelType = ChannelType.PRIVATE

    def __init__(self, content: Union[str, bytes], msg_type: MsgType = MsgType.TEXT, **kwargs):
        kwargs.update({"content": content, "msg_type": msg_type})
        super().__init__(**kwargs)


class QuoteMessage(BaseModel):
    message: Message
    sender: UserInfo


class EventChatMessage(BaseModel):
    id: str = ""
    sender: UserInfo
    group: Optional[GroupInfo] = None
    message: Message
    channel_type: ChannelType
    raw: Dict[str, Any] = {}
    quoted_message: Optional['QuoteMessage'] = None


class EventNewSubscriber(BaseModel):
    new_subscriber: UserInfo


class CallbackMessage(BaseModel):
    event_type: EventType
    event: Union[EventChatMessage, EventNewSubscriber]


class SendMessageRequest(BaseModel):
    receiver: List[str]
    msg_type: str

