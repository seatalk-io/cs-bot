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
import abc
from abc import ABCMeta
from typing import List, Dict, Any, Tuple, Optional

from cs_bot.protocol import CallbackMessage, Message, EventChatMessage


class BaseAdapter(metaclass=ABCMeta):
    @abc.abstractmethod
    def __init__(self, bot: 'CSBot', config: Dict[str, Any]):
        pass

    @abc.abstractmethod
    def get_response(self, raw_body: bytes, headers: Dict[str, str]) -> Any:
        pass

    @abc.abstractmethod
    def extract_event(self, raw_body: bytes, headers: Dict[str, str]) -> Optional[CallbackMessage]:
        pass

    @abc.abstractmethod
    def send(self, receiver_email: str, message: Message):
        pass

    @abc.abstractmethod
    def send_group(self, group_name: str, message: Message, mentioned_emails: Optional[List[str]] = None):
        pass

    @abc.abstractmethod
    def reply(self, event: EventChatMessage, message: Message, quote_reply: bool = False):
        pass
