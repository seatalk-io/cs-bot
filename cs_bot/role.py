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
from cs_bot.protocol import CallbackMessage, UserInfo


class BaseRole:
    def __init__(self, bot: 'CSBot', user_info: UserInfo):
        self.bot: 'CSBot' = bot
        self.sender: UserInfo = user_info

    @classmethod
    def extract_from(self, bot: 'CSBot', event: CallbackMessage):
        return

    def is_owner(self) -> bool:
        return self.sender.email in self.bot.config.owner_emails

    def is_developer(self) -> bool:
        return self.sender.email in self.bot.config.developers


class Role(BaseRole):
    def __init__(self, bot: 'CSBot', user_info: UserInfo):
        super(Role, self).__init__(bot, user_info)
