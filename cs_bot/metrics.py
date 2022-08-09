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
from typing import Iterable

from prometheus_client import Histogram


class Status(str, Enum):
    OK = "OK"
    NO_MATCH = "NoMatch"
    NO_REPLY = "NoReply"
    ERROR = "Error"

    @classmethod
    def values(cls) -> Iterable[str]:
        return map(lambda s: s.value, cls)


MessageHandled = Histogram("cs_bot_message_handled", "messages handled by the cs_bot", labelnames=['status'])


def report_message_handled(status: Status, time_cost: float):
    MessageHandled.labels(status.value).observe(time_cost)
