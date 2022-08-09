import enum

from pydantic import BaseModel

import cs_bot
from cs_bot import MessageSession, logger
from cs_bot.permissions import OWNER, DEVELOPER, ANYONE

plugin_alias = "echo"


class ReplyPrefix(str, enum.Enum):
    HI = "hi"
    YOU_SAID = "you said"


class Config(BaseModel):
    content: str = ""
    reply_prefix: ReplyPrefix


@cs_bot.on_plugin_loaded()
def on_loaded():
    logger.info("echo plugin loaded")


@cs_bot.on_plugin_unload()
def on_unload():
    logger.info("echo plugin unload")


@cs_bot.on_config_updated()
def on_config_updated(config: Config):
    logger.info("config updated: %s", config)


@cs_bot.on_prefix(["echo"], priority=77, permission=OWNER or DEVELOPER or ANYONE)
def echo(session: MessageSession):
    config: Config = cs_bot.get_config(plugin_alias)
    logger.info(f"receive message: {session.message.content}")
    session.send(session.sender.email, config.reply_prefix + session.message.content.lstrip("echo"))


if __name__ == '__main__':
    print(Config.schema_json())
