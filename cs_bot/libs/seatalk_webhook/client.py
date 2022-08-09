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
import threading
import time
from enum import Enum
from typing import List, Dict, Union, Optional

import requests


class WebhookMsgType(str, Enum):
    TEXT = "text"
    MARKDOWN = "markdown"
    IMAGE = "image"


class WebhookClient:
    def __init__(self, webhooks: List[str]):
        self.limit_helpers: Dict[str, int] = {webhook: int(time.time()) - 60 for webhook in webhooks}
        self.lock = threading.Lock()

    def _get_available_webhook(self) -> Optional[str]:
        with self.lock:
            now = int(time.time())
            available_webhooks = list(
                filter(lambda webhook: self.limit_helpers[webhook] < now, self.limit_helpers.keys()))
            if available_webhooks:
                webhook = available_webhooks[0]
                self.limit_helpers[webhook] += 1
                return webhook

    def send(self, message: Union[str, bytes], msg_type: WebhookMsgType = WebhookMsgType.TEXT):
        for i in range(len(self.limit_helpers)):
            webhook: str = self._get_available_webhook()
            if webhook is None:
                raise ResourceWarning("All webhooks have reached the request rate limit")
            res = requests.post(
                webhook,
                json={
                    "tag": msg_type.value,
                    msg_type.value: {
                        "content": base64.b64encode(message).decode() if WebhookMsgType == WebhookMsgType.IMAGE else message
                    }
                }
            )
            if res.status_code == 429:
                self._rate_limit_exceeded(webhook)
                continue
            res.raise_for_status()
            break

    def _rate_limit_exceeded(self, webhook: str):
        with self.lock:
            self.limit_helpers[webhook] += 60
