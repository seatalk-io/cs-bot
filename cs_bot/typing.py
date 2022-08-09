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
import typing as t

from cs_bot.protocol import CallbackMessage

PluginAPI_F = t.Callable[..., t.Any]
PluginAPI_D = t.Callable[[PluginAPI_F], PluginAPI_F]
EventHandler_F = t.Callable[[CallbackMessage], None]
LifecycleHook_F = t.Callable[..., None]
LifecycleHook_D = t.Callable[[], LifecycleHook_F]
PermPolicy = t.Callable[['Session'], bool]
Adapter_T = t.Type["Adapter"]

Export_F = t.Callable[[], t.Any]
Export_D = t.Callable[[Export_F], Export_F]

MatcherRule_F = t.Callable[['Session'], bool]
TextMatchRule_F = t.Callable[[t.List[str], str], bool]

PluginConfig_T = t.Type['Config']
PluginLoadedHook_F = t.Callable
PluginLoadedHook_D = t.Callable[[PluginLoadedHook_F], PluginLoadedHook_F]
PluginUnloadHook_F = t.Callable
PluginUnloadHook_D = t.Callable[[PluginUnloadHook_F], PluginUnloadHook_F]
PluginConfigUpdateHook_F = t.Callable[[t.Type['Config']], None]
PluginConfigUpdateHook_D = t.Callable[[PluginConfigUpdateHook_F], PluginConfigUpdateHook_F]

AutoUpdateConfig_D = t.Callable[[PluginConfig_T], PluginConfig_T]

SchedulerJob_F = t.Callable

Words_T = t.Union[str, t.List[str]]

MessageProcessor = t.Callable[['MessageSession'], None]
MessageProcessorHook_D = t.Callable[[MessageProcessor], MessageProcessor]

State_T = t.Type['State']
StateTimeoutCallback_F = t.Callable[[str, 'State'], t.Optional[t.Tuple['State', int]]]
StateTimeoutCallback_D = t.Callable[[StateTimeoutCallback_F], StateTimeoutCallback_F]
