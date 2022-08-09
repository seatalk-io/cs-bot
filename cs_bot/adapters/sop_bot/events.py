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
from typing import Union

from pydantic import BaseModel


class EventType(Enum):
    """
    EventType definition of the Event Callback from Seatalk Open Platform.
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    SINGLE_CHAT = "message_from_bot_subscriber"
    NEW_SUBSCRIBER = "new_bot_subscriber"
    VERIFICATION = "event_verification"


class Text(BaseModel):
    """
    TextMessage definition.
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    content: str


class ChatMessage(BaseModel):
    """
    Message definition.
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    tag: str
    text: Text


class EventSingleChat(BaseModel):
    """
    Event Definition of the Callback Event <message_from_bot_subscriber>.
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    employee_code: str
    message: ChatMessage


class EventNewSubscriber(BaseModel):
    """
    Event Definition of the Callback Event <new_bot_subscriber>.
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    employee_code: str


class EventURLVerification(BaseModel):
    """
    Event Definition of the Callback Event <event_verification>.
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    seatalk_challenge: str


class CallbackRequestBase(BaseModel):
    """
    Common Fields of the Event Callback Request.
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    event_id: str
    event_type: EventType
    timestamp: int
    app_id: str


class CallbackRequest(CallbackRequestBase):
    """
    Event Callback Request definition
    See details in https://open.seatalk.io/docs/messaging_messaging-events .
    """
    event: Union[EventSingleChat, EventNewSubscriber, EventURLVerification]
