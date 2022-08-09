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
import os
from typing import Type

import peewee as peewee

from cs_bot.models.database import get_db

TABLE_NAME_MAPPING = {
    "PluginConfig": "plugin_config",
    "KVRecord": "kv_record"
}


def table_name(model_class: Type[peewee.Model]):
    model_name = model_class.__name__
    return os.getenv(f"{model_name}TableName", TABLE_NAME_MAPPING[model_name])


class PluginConfig(peewee.Model):
    id = peewee.PrimaryKeyField()
    version = peewee.IntegerField()
    plugin_name = peewee.CharField()
    create_at = peewee.IntegerField()
    value = peewee.TextField()

    class Meta:
        database = get_db()
        table_function = table_name


class KVRecord(peewee.Model):
    id = peewee.PrimaryKeyField()
    key = peewee.CharField()
    value = peewee.TextField()

    class Meta:
        database = get_db()
        table_function = table_name


if __name__ == '__main__':
    pass
