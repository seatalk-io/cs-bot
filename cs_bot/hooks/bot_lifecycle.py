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

from typing import Set
from cs_bot.typing import LifecycleHook_F, LifecycleHook_D


class BotLifecycle:
    """
    BotLifecycle
    """

    def __init__(self):
        """

        """
        self._init_callbacks: Set[LifecycleHook_F] = set()

    def on_startup(self) -> LifecycleHook_D:
        """
        on_init
        :return: a decorator to use to register an bot initialization callback
        :rtype: LifecycleHook_D
        """

        def decorator(f: LifecycleHook_F):
            self._init_callbacks.add(f)
            return f

        return decorator

    def emit_startup(self):
        """
        Emit the init event, iterate all the callback functions and call.
        :return: None
        """
        for init_callback in self._init_callbacks:
            init_callback()
