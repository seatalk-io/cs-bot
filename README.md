# CSBot

## Introduction

**CSBot** is a framework used to develop SeaTalk Open Platform Bot APP. About Seatalk Open Platform, visit [open.seatalk.io](http://open.seatalk.io) to learn more.

SeaTalk Open Platform provides HTTP APIs to enable a bot to send messages to its subscribers. And when a bot receives a message from its subscriber, Seatalk Open Platform will send an HTTP request as a callback to the developer's server.

## Pre-requirements

### Python Version

We recommend using the latest version of Python. This project supports Python 3.7 and newer.

### Seatalk APP

To make you bot work, a SeaTalk Open Platform Bot APP is required. Follow this [link](https://open.seatalk.io/docs/quickly-build-a-bot) to create a bot APP.

## Quick Start

1. Create a python project
2. Install the cs_bot package
3. Create a folder `plugins`
4. Create python scripts `main.py` in the project root folder and `echo.py` in the `plugins` folder

Now, your project should look like:

```
├── plugins
│   └── echo.py
├── main.py
```

### Installation

#### Using pip

```shell
pip install "cs-bot @ git+https://github.com/seatalk-io/cs-bot.git@main"
```

#### Using poetry

```shell
poetry add git+ssh://git@github.com/seatalk-io/cs-bot.git
```

### Write your first bot server

In the project you created above, you'll be using `cs_bot` framework, so every python module can be loaded as a **plugin**. This framework uses plugins to manage message handling logics.

#### Write a plugin

```python
# plugins/echo.py
import cs_bot
from cs_bot import MessageSession, logger
from cs_bot.permissions import ANYONE


@cs_bot.on_prefix(["echo"], permission=ANYONE)
def echo(session: MessageSession):
    logger.info(f"receive message: {session.message.content}")
    session.send(session.sender.email, session.message.content.lstrip("echo"))

```

#### main.py

```python
# main.py
import cs_bot
from cs_bot import StartupConfig
from cs_bot.adapters import sop_bot

config = {
    "adapter": {"app_id": "your_app_id", "app_secret": "your_app_secret", "signing_secret": "your_signing_secret"}
}
cs_bot.init(StartupConfig.parse_obj(config))
cs_bot.register_adapter(sop_bot.Adapter)
cs_bot.load_plugin("plugins.echo")

if __name__ == '__main__':
    cs_bot.run(host="your_host_ip", port=your_port)

```

1. Visit the [SeaTalk Open Platform](https://open.seatalk.io/), find your APP and replace `your_app_id`, `your_app_secret` with the ones displayed on the `Basic Info & Credentials` page
2. Stay at the [SeaTalk Open Platform](https://open.seatalk.io/), find `your app -> Event Callback -> Signing Secret`, copy the signing secret and replace the `your_signing_secret` with it
3. Replace `your_host_ip` and `your_port` to your public IP and your port
4. Run the python script `python main.py`

### Configure the Callback URL

1. Open the SeaTalk Open Platform, find `your app -> Event Callback -> Event Callback URL`, edit the Event Callback URL
   to `http://your_host_ip:your_port/callback` and save
2. Open your seatalk and click the `search contact`, find your bot and subscribe
3. Send `echo hello world` and then your bot should reply a `hello world` to you

### What happened

* `cs_bot.init()` instantiates and initializes the global default CSBot instance
* `cs_bot.register_adapter(sop_bot.Adapter)` registers an adapter class named `sop_bot.Adapter` for the global default
  CSBot instance. (An Adapter is used to adapt various Event Callback Protocol to the unified CSBot Message Protocol)
* `cs_bot.load_plugin("plugins.echo")` loads a plugin named `plugins.echo` for the global default CSBot
  instance. <br/> This plugin allows user trigger a message process procedure using `echo xxx` and the bot should
  reply an `xxx`
* `cs_bot.run(host="your_host_ip")` starts the dev server

## Advanced

### StartupConfig

Part of features of `CSBot` (like FSM which will be mentioned later) depend on the `database` and the `redis`. To use these features the developer need to initialize the `database` and the `redis` dependency properly by setting up the StartupConfig.  

The `StartupConfig` is an initialization configuration definition used to init the `CSBot`. It is a subclass of the `pydantic.BaseModel`, so it has following `classmethod` available to load a config file.

* `StartupConfig.parse_file(file_path: str)` loads a json structured config from a file
* `StartupConfig.parse_raw(config_str: str)` loads a json structured config from a json string
* `StartupConfig.parse_obj(config_dict: dict)` loads a json structured config from a python dict

The full example of the json structured config is as following:
`config.json`

```json
{
  "db": {
    "database": "default_db",
    "port": 3306,
    "host": "127.0.0.1",
    "user": "",
    "password": "",
    "driver": "mysql or sqlite"
  },
  "redis": {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 1
  },
  "adapter": {
    "app_id": "",
    "app_secret": "",
    "signing_secret": ""
  },
  "callback_path": "/callback"
}
```

The following code shows how to load this `config.json` and use it to initialize the `CSBot`.

```python
import cs_bot
from cs_bot import StartupConfig

cs_bot.init(StartupConfig.parse_file("config.json"))
```


### Matcher

`cs_bot.Matcher` is a concept that matches messages and processes messages.

#### Process a text message

`cs_bot` provides following builtin decorator to register message process functions. To learn more builtin matcher rules, see [API Reference](#API Reference).

```python
# plugins/clock.py
import cs_bot
from cs_bot import MessageSession
from datetime import datetime


@cs_bot.on_keyword(["time"])
def time_teller(sess: MessageSession):
    clock: str = datetime.now().strftime("%H:%M:%s")
    sess.reply(f"Now it is {clock}")
```

#### Process an image/sticker message

```python
# plugins/sticker.py
import cs_bot
from cs_bot import MessageSession
from cs_bot import logger


@cs_bot.on_image()
def time_teller(sess: MessageSession):
    logger.info("bot received a message msg_type: %s", sess.message.msg_type)
    sess.reply(f"you sent a image")
    sess.reply(sess.message)  # send the image back
```

#### Priority

The matchers are trying to match the incoming message with the order they are registered.

Sometimes more than one matcher may match one same message, to make sure the mached matcher executed in a correct order, we introduce the priority argument for the Matcher.

```python
# plugin/priority.py
import cs_bot
from cs_bot import MessageSession


@cs_bot.on_keyword("command", priority=1)
def the_second_command(sess: MessageSession):
    # this command should not be matched
    pass


@cs_bot.on_keyword("command", priority=2)
def the_first_command(sess: MessageSession):
    # this command should be matched
    sess.reply("the first command is triggered")
    # abort the other matchers
    sess.abort()
```

#### Send a message

`cs_bot` provides some global functions to send messages.

```python
import cs_bot

# send to the single receiver
cs_bot.send("receiver-email@gmail.com", "message content")
# send to multi receivers
cs_bot.send(["receiver1@gmail.com", "receiver2@gmail.com"], "message content")
```

### Permission

Permission is a rule to determine whether a message can trigger the specified matcher.

#### Builtin Permissions

There are few builtin permissions in `cs_bot`: `OWNER`/`DEVELOPER`/`ANYONE`. Permission class support the `or` and the `and` operation.

The default permission of a matcher is always the `ANYONE` which means everyone can trigger it.

To create a matcher that only can be triggered by the owner or developer.

```python
import cs_bot
from cs_bot import MessageSession
from cs_bot.permissions import OWNER, DEVELOPER


@cs_bot.on_exact("system status", permission=OWNER or DEVELOPER)
def admin_command(sess: MessageSession):
    pass
```

### Scheduler

`cs_bot` provides a builtin scheduler based on the [schedule](https://github.com/dbader/schedule) lib.

`cs_bot.scheduler` uses a ThreadPoolExecutor to enable the concurrency of multiple tasks.

```python
# plugins/scheduler.py
import cs_bot


def first_job(number: int):
    print(number)


cs_bot.every(10).seconds.do(first_job, 1)
```

See advanced usages in [schedule document](https://schedule.readthedocs.io/).


### State and FSM

`CSBot` provides an FSM implement to help developer to maintain the customer states.

To use the FSM, the developer need to define a state class first. A state definition should be like the following:

> ⚠️ The FSM depends on the redis, do initialize the redis dependency before using the FSM.
>
> See [Advanced -> StartupConfig] to set up the configuration of the redis dependency.

```python
from cs_bot.session import State


class CustomerState(State):
    IDLE = "idle"
    CONSULTING = "consulting"

    @classmethod
    def default_state(cls) -> 'State':
        return cls.CONSULTING
```

After a state class is defined, the developer need to register the state to obtain an FSM instance.

`fsm: FSM = cs_bot.register_fsm("customer_state", CustomerState)`

Then the developer can use the state within a matcher.

```python
import cs_bot
from cs_bot import MessageSession


@cs_bot.on_keyword("customer service")
def the_second_command(sess: MessageSession):
    state = sess.get_state(CustomerState)
    if state == CustomerState.IDLE:
        sess.store_state(CustomerState.CONSULTING, 600)
        sess.reply("you have entered the consulting state")
```

To handle the state timeout events, the developer can use the `fsm.handle_timeout()` decorator to register an unified state timeout event handler.

The complete code is as the following:

```python
import cs_bot
from cs_bot.session import State
from typing import Optional


class CustomerState(State):
    IDLE = "idle"
    CONSULTING = "consulting"

    @classmethod
    def default_state(cls) -> 'State':
        return cls.CONSULTING


customer_state_fsm = cs_bot.register_fsm("customer_state", CustomerState)
customer_state_fsm.handle_time_out()


def handle_timeout(email: str, timeout_state: CustomerState) -> Optional[CustomerState]:
    # do something with state timeout event
    pass
```

## API Reference

See reference in [api_reference.md](api_reference.md)

## License

* Apache 2.0
