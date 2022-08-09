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
import re
from functools import reduce

from cs_bot.session import MessageSession
from cs_bot.protocol import Message, MsgType, CallbackMessage, EventType
from cs_bot.typing import MatcherRule_F, Words_T, TextMatchRule_F


def rule_template(word: Words_T, f: TextMatchRule_F) -> MatcherRule_F:
    def match(session: MessageSession) -> bool:
        event: CallbackMessage = session.event
        msg: Message = event.event.message
        if isinstance(word, list):
            words = word
        else:
            words = [word]
        return event.event_type == EventType.NEW_CHAT_MESSAGE and \
               msg.msg_type == MsgType.TEXT and \
               f(words, msg.content)

    return match


def rule_on_prefix(prefix: Words_T) -> MatcherRule_F:
    return rule_template(
        prefix, lambda words, content: reduce(lambda a, b: a or b, map(lambda p: content.startswith(p), words))
    )


def rule_on_regex(regex: Words_T) -> MatcherRule_F:
    return rule_template(
        regex, lambda words, content: reduce(lambda a, b: a or b, map(lambda p: bool(re.match(p, content)), words))
    )


def rule_on_keyword(keyword: Words_T) -> MatcherRule_F:
    return rule_template(
        keyword,
        lambda words, content: reduce(lambda a, b: a or b, map(lambda p: p in content, words))
    )


def rule_on_exact(keyword: Words_T) -> MatcherRule_F:
    return rule_template(
        keyword,
        lambda words, content: reduce(lambda a, b: a or b, map(lambda p: p == content, words))
    )
