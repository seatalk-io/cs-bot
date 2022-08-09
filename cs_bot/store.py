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
from typing import Dict, Any, Optional, Iterable, Tuple

import peewee
from peewee import SqliteDatabase, MySQLDatabase
from playhouse.shortcuts import ReconnectMixin
from redis import Redis

from cs_bot.log import logger
from cs_bot.configs.startup_config import DBConfig, RedisConfig
from cs_bot.models.config import KVRecord, PluginConfig, TABLE_NAME_MAPPING
from cs_bot.models.database import get_db


class ReconnectMySQLDatabase(ReconnectMixin, peewee.MySQLDatabase):
    pass


class Storage:
    db_driver: str = "sqlite"

    @classmethod
    def init(cls, config: DBConfig):
        cls.db_driver = config.driver
        if config.driver == "sqlite":
            get_db().initialize(SqliteDatabase(config.database, pragmas={'journal_mode': 'wal'}))
        elif config.driver == "mysql":
            get_db().initialize(
                ReconnectMySQLDatabase(config.database, user=config.user, password=config.password, host=config.host,
                                       port=config.port))
        if config.need_migration:
            cls.init_migration()

    @classmethod
    def init_migration(cls):
        logger.info("[Store] migrating")
        with get_db() as db:
            db.create_tables([
                PluginConfig,
                KVRecord,
            ])

    @classmethod
    def set(cls, key: str, value: str):
        record: KVRecord = KVRecord.get_or_none(key=key)
        if record is None:
            record = KVRecord()
        record.key = key
        record.value = value
        record.save()

    @classmethod
    def get(cls, key: str) -> Optional[str]:
        record: KVRecord = KVRecord.get_or_none(key=key)
        if record is None:
            return None
        return record.value

    @classmethod
    def delete(cls, key: str) -> bool:
        record: KVRecord = KVRecord.get_or_none(key=key)
        if record is not None:
            record.delete()
            return True
        return False

    @classmethod
    def range(cls, start_key: str, end_key: str,
              include_start_key: bool = True, include_end_key: bool = True) -> Iterable[Tuple[str, str]]:
        if include_start_key:
            condition = KVRecord.key >= start_key
        else:
            condition = KVRecord.key > start_key
        if include_end_key:
            condition = condition and (KVRecord.key <= end_key)
        else:
            condition = condition and (KVRecord.key < end_key)

        return map(lambda r: (r.key, r.value), KVRecord.select().where(condition))


class CacheManager(Redis):
    def __init__(self, config: RedisConfig):
        super().__init__(**config.dict())
        self._storage: Dict = {}
