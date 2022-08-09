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
import datetime
import time
from enum import Enum
from typing import Any, Dict, Union, Optional, List, Iterable, Tuple

from cs_bot.store import CacheManager
from cs_bot.helper import md5
from cs_bot.protocol import CallbackMessage, Message, UserInfo, ChannelType
from cs_bot.role import Role
from cs_bot.typing import StateTimeoutCallback_F, StateTimeoutCallback_D, State_T


class State(str, Enum):

    @classmethod
    @abc.abstractmethod
    def default_state(cls) -> 'State':
        pass

    @classmethod
    def from_str(cls, s: Union[str, bytes]) -> 'State':
        if isinstance(s, bytes):
            s = s.decode()
        try:
            return cls(s)
        except:
            return cls.default_state()


class FSM:
    def __init__(self, bot: 'CSBot', fsm_name: str, state_class: State_T):
        if not issubclass(state_class, State):
            raise ValueError(
                f"invalid state_class. expect a subclass of the cs_bot.State, got {state_class.__name__} instead"
            )
        self.bot: 'CSBot' = bot
        self.maintain_job = None
        self.state_class = state_class
        self.default_state: Optional[State_T] = None
        self.fsm_name: str = fsm_name
        self.state_set_key: str = f"_state_set_{self.fsm_name}"
        self.timeout_handler: Optional[StateTimeoutCallback_F] = None
        self._start_maintain_states()

    def handle_time_out(self) -> StateTimeoutCallback_D:
        def decorator(callback: StateTimeoutCallback_F) -> StateTimeoutCallback_F:
            self.timeout_handler = callback
            return callback

        return decorator

    def state_key(self, email: str) -> str:
        return f"_state_{self.fsm_name}_{email}"

    def store_state(self, customer_email: str, state: State, timeout: int):
        pipline = self.bot.cache.pipeline(transaction=True)
        pipline.zadd(self.state_set_key, {customer_email: int(time.time()) + timeout})
        pipline.set(self.state_key(customer_email), state.value)
        pipline.execute()

    def remove_expired_states(self) -> Iterable[Tuple[str, State]]:
        """
        Remove all the timeout states from the ZSET and trigger the FSM timeout handler.
        :return: an Iterable object of Tuple (email: str, previous_state: State)
        """
        except_start_time = int(time.time())
        expired_session_emails: List[bytes] = self.bot.cache.zrangebyscore(
            self.state_set_key, float('-inf'), except_start_time
        )
        if expired_session_emails:
            pipeline = self.bot.cache.pipeline(transaction=True)
            pipeline.zrem(self.state_set_key, *expired_session_emails)
            state_keys = list(map(lambda e: self.state_key(e.decode()), expired_session_emails))
            pipeline.mget(keys=state_keys)
            pipeline.delete(*state_keys)
            removed, states, deleted = pipeline.execute()
            return zip(
                map(
                    lambda e: e.decode(), expired_session_emails),
                map(lambda s: self.state_class.from_str(s), states)
            )
        return []

    def clear_state(self, customer_email: str) -> Tuple[Optional[State], bool]:
        """
        Reset the state to the default_state for the specified user
        :param customer_email: email
        :return: Tuple (previous_state, removed or not)
        """
        pipline = self.bot.cache.pipeline(transaction=True)
        pipline.zrem(self.state_set_key, customer_email)
        pipline.get(self.state_key(customer_email))
        pipline.delete(self.state_key(customer_email))
        removed_rows, state, deleted_rows = pipline.execute()
        try:
            return self.state_class.from_str(state), removed_rows > 0 and deleted_rows > 0
        except:
            return self.state_class.default_state(), False

    def get_state(self, custom_email: str) -> State:
        state: Optional[State] = None
        state_name: Optional[str] = self.bot.cache.get(self.state_key(custom_email))
        if state_name is not None:
            state = self.state_class.from_str(state_name)
        return state or self.state_class.default_state()

    def maintain_states(self):
        expired_states = self.remove_expired_states()
        for email, state_str in expired_states:
            if self.timeout_handler is not None:
                result = self.timeout_handler(email, self.state_class.from_str(state_str))
                if result is not None and isinstance(result, tuple) and len(result) == 2:
                    new_state_str, timeout = result
                    self.store_state(email, self.state_class.from_str(new_state_str), timeout)

    def _start_maintain_states(self):
        self.maintain_job = self.bot.scheduler.every().second.do(self.maintain_states)

    def __del__(self):
        if self.maintain_job is not None:
            self.bot.scheduler.cancel_job(self.maintain_job)


class BaseSession:
    def __init__(self, bot: 'CSBot', event: CallbackMessage, session_manager: 'SessionManager'):
        self._bot: 'CSBot' = bot
        self._state: Dict[str, Any] = dict()
        self._event: CallbackMessage = event
        self._aborted: bool = False
        self._session_manager = session_manager

    @property
    def event(self) -> CallbackMessage:
        return self._event

    @property
    def state(self) -> Dict[str, Any]:
        return self._state

    @property
    def aborted(self) -> bool:
        return self._aborted

    def abort(self):
        self._aborted = True

    def stop(self):
        pass


class MessageSession(BaseSession):
    _TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, bot: 'CSBot', event: CallbackMessage, session_manager: 'SessionManager'):
        super(MessageSession, self).__init__(bot, event, session_manager)
        self.sender: UserInfo = event.event.sender
        self.message: Message = event.event.message
        self.channel_type: ChannelType = event.event.channel_type
        self.role = Role(bot, event.event.sender)
        self.reply_count: int = 0
        self.state_cache: Dict[State_T, 'State'] = {}

    def send(self, receiver_email: Union[str, List[str]], message: Union[str, Message]):
        self.reply_count += 1
        return self._bot.send(receiver_email, message)

    def reply(self, message: Union[str, Message], quote_reply: bool = False):
        self.reply_count += 1
        return self._bot.reply(self.event.event, message, quote_reply)

    def _query_state(self, state_class: Union[State_T, str]) -> Optional['State']:
        fsm: FSM = self._bot.get_fsm(state_class)
        state = fsm.get_state(self.sender.email)
        self.state_cache[state_class] = state
        return state

    def get_state(self, state_class: Union[State_T, str]) -> 'State':
        cached_state = self.state_cache.get(state_class, None)
        return cached_state or self._query_state(state_class)

    @property
    def id(self):
        return "message-session-" + md5(f"{self.sender.email}&{self.channel_type.value}")

    @property
    def last_message_time(self) -> Optional[datetime.datetime]:
        v = self._session_manager.cache.get(self.id)
        self._session_manager.cache.set(self.id, datetime.datetime.now().strftime(self._TIME_FORMAT))
        if v is None:
            return v
        return datetime.datetime.strptime(v, self._TIME_FORMAT)

    def stop(self):
        super(MessageSession, self).stop()
        self._session_manager.cache.delete(self.id)


class FriendListChangeSession(BaseSession):
    def __init__(self, bot: 'CSBot', cm: CallbackMessage, session_manager: 'SessionManager'):
        super(FriendListChangeSession, self).__init__(bot, cm, session_manager)
        self.new_subscriber: UserInfo = cm.event.new_subscriber


class SessionManager:
    def __init__(self, cache_manager: CacheManager):
        self.cache: CacheManager = cache_manager
