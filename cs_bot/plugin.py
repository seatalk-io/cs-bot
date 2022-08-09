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
import contextlib
import importlib
import json
import time
from types import ModuleType
from typing import Optional, Dict, List, Set, Type, Any

from pydantic import BaseModel, ValidationError

from cs_bot import APIAuth
from cs_bot.log import logger
from cs_bot.models.config import PluginConfig
from cs_bot.permissions import Permission
from cs_bot.protocol import MsgType
from cs_bot.session import MessageSession
from cs_bot.hooks.matcher import Matcher
from cs_bot.rule import rule_on_prefix, rule_on_regex, rule_on_keyword, rule_on_exact
from cs_bot.typing import PluginAPI_F, MessageProcessor, MessageProcessorHook_D, LifecycleHook_F, \
    PluginConfigUpdateHook_F, \
    LifecycleHook_D, PluginConfigUpdateHook_D, PluginLoadedHook_D, PluginLoadedHook_F, PluginUnloadHook_F, \
    PluginUnloadHook_D, Words_T, PluginAPI_D, PluginConfig_T, AutoUpdateConfig_D, Export_D, Export_F


class ConfigUpdateCallback:
    def __init__(self, f: PluginConfigUpdateHook_F, immediate: bool = False):
        self.f = f
        self.immediate = immediate


class PluginLifecycle:
    def __init__(self):
        self.onload_callbacks: List[LifecycleHook_F] = []
        self.unload_callbacks: List[LifecycleHook_F] = []
        self.config_update_callback: List[ConfigUpdateCallback] = []

    def on_load(self) -> LifecycleHook_D:
        def decorator(f: LifecycleHook_F) -> LifecycleHook_F:
            self.onload_callbacks.append(f)
            return f

        return decorator

    def on_unload(self) -> LifecycleHook_D:
        def decorator(f: LifecycleHook_F) -> LifecycleHook_F:
            self.unload_callbacks.append(f)
            return f

        return decorator

    def emit_on_load(self):
        for callback in self.onload_callbacks:
            callback()

    def emit_on_unload(self):
        for callback in self.unload_callbacks:
            callback()

    def emit_config_updated(self, new, is_init: bool = False):
        for callback in filter(lambda c: not is_init or c.immediate, self.config_update_callback):
            callback.f(new)

    def on_plugin_config_update(self, immediate: bool = False) -> PluginConfigUpdateHook_D:
        def decorator(f: PluginConfigUpdateHook_F) -> PluginConfigUpdateHook_F:
            self.config_update_callback.append(ConfigUpdateCallback(f=f, immediate=immediate))
            return f

        return decorator


class PluginAPI:
    def __init__(self, handler: PluginAPI_F, auth_role: APIAuth):
        self.handler: PluginAPI_F = handler
        self.auth_role: APIAuth = auth_role


class Plugin:
    def __init__(self, module: ModuleType, name: str,
                 lifecycle: PluginLifecycle, custom_api: Dict[str, Dict[str, PluginAPI]],
                 config_class: Optional[Type['Config']], config, config_auto_sync: bool,
                 exported_functions: Dict[str, Export_F]):
        self.module: ModuleType = module
        self.name: str = name
        self.config: Optional[BaseModel] = config
        self.config_class: Optional[Type['Config']] = config_class
        self.matchers: List[Matcher] = []
        self.lifecycle: PluginLifecycle = lifecycle
        self.config_auto_sync: bool = config_auto_sync
        self.exported_functions: Dict[str, Export_F] = exported_functions

        self.enabled: bool = True
        if self.config_class is not None and self.config is None:
            previous_config = {}
            last_config_version: Optional[PluginConfig] = PluginConfig.select().\
                where(PluginConfig.plugin_name == self.name).order_by(-PluginConfig.version).get_or_none()
            if last_config_version is not None:
                previous_config = json.loads(last_config_version.value)
            try:
                logger.info("try to use the previous config: %s", previous_config)
                self.config = config_class(**previous_config)
            except ValidationError as e:
                self.enabled = False
                logger.fatal(f"plugin [{self.name}] does not define the default value of the Config")
        # {
        #   "method": {"path": handler}
        # }
        self.custom_apis: Dict[str, Dict[str, PluginAPI]] = custom_api

    def get_api_handler(self, api_path: str, method: str) -> Optional[PluginAPI]:
        return self.custom_apis.get(method, {}).get(api_path, None)

    def setup_auto_sync_lock(self):
        pass

    def get_exported_func(self, function_name: str) -> Optional[Export_F]:
        return self.exported_functions.get(function_name, None)

    def to_json(self) -> Dict:
        return {
            "module_path": self.module.__name__,
            "plugin_alias": self.name,
            "has_config_schema": self.config_class is not None,
            "enabled": self.enabled
        }

    def update_config(self, new_config: Dict) -> None:
        if self.config_class is not None:
            last_config: PluginConfig = PluginConfig.select().where(PluginConfig.plugin_name == self.name). \
                order_by(PluginConfig.version.desc()).get_or_none()
            new_version = (0 if last_config is None else last_config.version) + 1
            PluginConfig.create(
                version=new_version, create_at=int(time.time()), plugin_name=self.name, value=json.dumps(new_config)
            )
            self.config = self.config_class(**new_config)
            self.lifecycle.emit_config_updated(self.config)


class PluginManager:
    plugins: Dict[str, Plugin] = dict()

    @classmethod
    def load_plugin(cls, module_path: str) -> Optional[Plugin]:
        with cls.TempPluginTemplate.enter_plugin():
            cls.TempPluginTemplate.module = importlib.import_module(module_path)
        plugin: Plugin = cls.TempPluginTemplate.create_plugin()
        if plugin.name in cls.plugins:
            raise ValueError(f"plugin [{plugin.name}] has already been registered")
        cls.plugins[plugin.name] = plugin

        logger.info(f"[PluginManager] load plugin [{plugin.name}] from \"{module_path}\"")
        plugin.lifecycle.emit_on_load()
        if plugin.config is not None:
            plugin.lifecycle.emit_config_updated(plugin.config, is_init=True)
        return plugin

    @classmethod
    def get_plugin_by_name(cls, plugin_name: str) -> Optional[Plugin]:
        return cls.plugins.get(plugin_name, None)

    @classmethod
    def on_prefix(cls, prefix: Words_T, permission: Optional[Permission], priority) -> MessageProcessorHook_D:
        def inner(p: MessageProcessor):
            cls.TempPluginTemplate.matchers.add(
                Matcher(rule_on_prefix(prefix), permission, priority, p)
            )
            return p

        return inner

    @classmethod
    def on_regex(cls, pattern: Words_T, permission: Optional[Permission], priority: int):
        def inner(p: MessageProcessor):
            cls.TempPluginTemplate.matchers.add(
                Matcher(rule_on_regex(pattern), permission, priority, p)
            )
            return p

        return inner

    @classmethod
    def on_keyword(cls, keyword: Words_T, permission: Optional[Permission], priority: int):
        def inner(p: MessageProcessor):
            cls.TempPluginTemplate.matchers.add(
                Matcher(rule_on_keyword(keyword), permission, priority, p)
            )
            return p

        return inner

    @classmethod
    def on_exact(cls, pattern: Words_T, permission: Optional[Permission], priority: int):
        def inner(p: MessageProcessor):
            cls.TempPluginTemplate.matchers.add(
                Matcher(rule_on_exact(pattern), permission, priority, p)
            )
            return p

        return inner

    @classmethod
    def on_image(cls, permission: Optional[Permission], priority: int):
        def inner(p: MessageProcessor):
            cls.TempPluginTemplate.matchers.add(
                Matcher(lambda s: s.message.msg_type in {MsgType.IMAGE, MsgType.STICKER_C}, permission, priority, p)
            )
            return p

        return inner

    @classmethod
    def on_any(cls, permission: Optional[Permission], priority: int):
        def inner(p: MessageProcessor):
            cls.TempPluginTemplate.matchers.add(
                Matcher(lambda s: True, permission, priority, p)
            )
            return p

        return inner

    @classmethod
    def export(cls, alias: Optional[str] = None) -> Export_D:
        def deco(f: Export_F) -> Export_F:
            exported_name = alias or f.__name__
            cls.TempPluginTemplate.exported_functions[exported_name] = f
            return f

        return deco

    @classmethod
    def on_plugin_loaded(cls) -> PluginLoadedHook_D:
        return cls.TempPluginTemplate.plugin_lifecycle.on_load()

    @classmethod
    def on_plugin_unloaded(cls) -> PluginUnloadHook_D:
        return cls.TempPluginTemplate.plugin_lifecycle.on_unload()

    @classmethod
    def on_config_updated(cls, immediate: bool = False) -> PluginUnloadHook_D:
        return cls.TempPluginTemplate.plugin_lifecycle.on_plugin_config_update(immediate)

    @classmethod
    def get_config(cls, plugin_name: str) -> Optional[PluginConfig_T]:
        plugin = cls.get_plugin_by_name(plugin_name)
        if plugin is None:
            raise ValueError(f"plugin [{plugin_name}] is not found")
        if plugin.config is None:
            raise ValueError(f"Config class is not defined on the plugin [{plugin_name}]")
        return plugin.config

    @classmethod
    def register_plugin_api(cls, path: str, methods: List[str], auth_role: APIAuth = APIAuth.Anonymous) -> PluginAPI_D:
        def decorator(f: PluginAPI_F) -> PluginAPI_F:
            api_mapping = cls.TempPluginTemplate.custom_apis
            for method in methods:
                api_mapping[method] = api_mapping.get(method, {})
                api_mapping[method][path] = PluginAPI(f, auth_role)
            return PluginAPI_F

        return decorator

    class TempPluginTemplate:
        """
        plugin template singleton
        """
        in_plugin: bool = False
        plugin_lifecycle: PluginLifecycle = PluginLifecycle()
        matchers: Set[Matcher] = set()
        module: Optional[ModuleType] = None
        config: Optional[PluginConfig_T] = None
        config_class: Optional[Type] = None
        config_auto_sync: bool = False
        custom_apis: Dict[str, Dict[str, PluginAPI]] = {}
        exported_functions: Dict[str, Any] = {}

        @classmethod
        @contextlib.contextmanager
        def enter_plugin(cls):
            try:
                cls.clear()
                cls.in_plugin = True
                yield
            finally:
                cls.in_plugin = False

        @classmethod
        def clear(cls):
            cls.plugin_lifecycle = PluginLifecycle()
            cls.matchers.clear()
            cls.module = None
            cls.config = None
            cls.config_class = None
            cls.custom_apis = {}
            cls.exported_functions = {}

        @classmethod
        def create_plugin(cls) -> Plugin:
            try:
                module_name = cls.module.__getattribute__("plugin_alias")
            except Exception as e:
                module_name = cls.module.__name__
            plugin = Plugin(
                module=cls.module,
                name=module_name,
                lifecycle=cls.plugin_lifecycle,
                custom_api=cls.custom_apis,
                config_class=cls.get_config_class(),
                config=cls.config,
                config_auto_sync=cls.config_auto_sync,
                exported_functions=cls.exported_functions
            )
            for matcher in cls.matchers:
                plugin.matchers.append(matcher)
            return plugin

        @classmethod
        def get_config_class(cls) -> Optional[Type['Config']]:
            try:
                config_class = cls.module.__getattribute__("Config")
                if issubclass(config_class, BaseModel):
                    return config_class
            except:
                logger.warning(f"Config class is not defined by the plugin [{cls.module.__name__}]")
                return None


# plugin helpers

def filter_matchers(sess: MessageSession) -> List[Matcher]:
    matchers: List[Matcher] = list()
    for plugin_name, plugin in PluginManager.plugins.items():
        if not plugin.enabled:
            continue
        for matcher in plugin.matchers:
            if matcher.test(sess):
                matchers.append(matcher)
    return sorted(matchers, key=lambda m: -m.priority)
