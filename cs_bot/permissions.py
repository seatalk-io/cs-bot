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
from cs_bot.session import MessageSession
from cs_bot.typing import PermPolicy


class Permission:
    """
    Permission is a rule to determined whether a message can trigger the specified Matcher.
    """

    def __init__(self, policy: PermPolicy):
        self.policy: PermPolicy = policy

    def allow(self, session: MessageSession) -> bool:
        """
        this method would be called to test whether the session has the permission to trigger the Matcher procedure.
        :param session: the incoming session to be tested
        :return: a bool value indicate the session has the permission or not
        """
        return self.policy(session)

    def __and__(self, other: 'Permission') -> 'Permission':
        def wrapped_policy(session: MessageSession):
            return self.allow(session) and other.allow(session)

        return Permission(policy=wrapped_policy)

    def __or__(self, other: 'Permission') -> 'Permission':
        def wrapped_policy(session: MessageSession):
            return self.allow(session) or other.allow(session)

        return Permission(policy=wrapped_policy)


OWNER = Permission(lambda s: s.role.is_owner())
DEVELOPER = Permission(lambda s: s.role.is_developer())
ANYONE = Permission(lambda s: True)
