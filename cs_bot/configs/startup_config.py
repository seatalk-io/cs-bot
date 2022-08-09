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
from typing import List, Any, Dict
from pydantic import BaseModel

_DEFAULT_SQLITE_DB = "cs_bot.db"
_DRIVER_SQLITE = "sqlite"


class DBConfig(BaseModel):
    """
    DBConfig
    driver: "mysql" or "sqlite" are available
    """
    database: str = _DEFAULT_SQLITE_DB
    port: int = 0
    host: str = "127.0.0.1"
    user: str = ""
    password: str = ""
    driver: str = _DRIVER_SQLITE

    need_migration: bool = False


class RedisConfig(BaseModel):
    """
    RedisConfig
    """
    host: str = "127.0.0.1"
    port: int = 6379
    db: int = 0


class StartupConfig(BaseModel):
    """
    Startup Config definition of the CSBot
    """
    db: DBConfig = DBConfig()
    redis: RedisConfig = RedisConfig()

    jwt_secret: str = ""

    adapter: Dict[str, Any] = {}
    callback_path: str = "/callback"
    signing_secret: str = ""
    debug = False
    max_scheduler_workers: int = 4
    max_msg_handler_workers: int = 32
    owner_emails: List[str] = []
    developers: List[str] = []
    webhooks: List[str] = []


DEFAULT_STARTUP_CONFIG: StartupConfig = StartupConfig()
