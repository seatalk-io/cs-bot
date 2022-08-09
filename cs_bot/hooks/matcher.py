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
from typing import Optional
from cs_bot.permissions import Permission, ANYONE
from cs_bot.session import MessageSession
from cs_bot.typing import MatcherRule_F, MessageProcessor


class Matcher:
    """
    Base Matcher Definition
    A matcher has 3️ duties
    1⃣️ To tell whether the session matches the rule.
    2⃣️ To tell whether the session.role has permission to trigger the message process procedure.
    3⃣️ Process the message.
    """

    def __init__(self, rule: MatcherRule_F, permission: Optional[Permission], priority: int,
                 processor: MessageProcessor):
        """
        init a new matcher / message process procedure
        :param rule: A function to tell whether a matcher is matched with the input session.
        :param permission: Used to judge whether a session has the permission to trigger a specified matcher.
        :param priority: priority decides the execution order of all matched matchers.
        :param processor: the function to call to process the incoming session.
        """
        self.rule: MatcherRule_F = rule
        self.permission: Permission = permission or ANYONE
        self.processor: MessageProcessor = processor
        self.priority: int = priority

    def test(self, session: MessageSession) -> bool:
        """
        tell whether the session match the current matcher
        :param session: the incoming session
        :return: True on matched otherwise False
        """
        return self.rule(session) and self._check_perm(session)

    def _check_perm(self, session: MessageSession) -> bool:
        """
        Tell whether the session has permission to trigger the message process procedure
        :param session: the incoming session
        :return: True on session.role has the permission otherwise False
        """
        return self.permission.allow(session)

    def process(self, session: MessageSession):
        """
        Process the incoming session, where the real logic should be set
        :param session: the incoming session
        :return: None
        """
        return self.processor(session)
