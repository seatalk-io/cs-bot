Table of Contents
=================


* [<kbd>module</kbd> adapters](#module-adapters)
* [<kbd>module</kbd> adapters.shopee_imbot](#module-adaptersshopee_imbot)
   * [<kbd>class</kbd> ReceiveNewMessageRequest](#class-receivenewmessagerequest)
   * [<kbd>class</kbd> Adapter](#class-adapter)
      * [<kbd>method</kbd> __init__](#method-__init__-1)
      * [<kbd>method</kbd> encoded_content](#method-encoded_content)
      * [<kbd>method</kbd> extract_event](#method-extract_event-1)
      * [<kbd>method</kbd> get_response](#method-get_response-1)
      * [<kbd>method</kbd> reply](#method-reply-1)
      * [<kbd>method</kbd> send](#method-send-1)
      * [<kbd>method</kbd> send_group](#method-send_group-1)
* [<kbd>module</kbd> adapters.sop_bot](#module-adapterssop_bot)
   * [<kbd>class</kbd> Adapter](#class-adapter-1)
      * [<kbd>method</kbd> __init__](#method-__init__-2)
      * [<kbd>method</kbd> extract_event](#method-extract_event-2)
      * [<kbd>method</kbd> get_response](#method-get_response-2)
      * [<kbd>method</kbd> get_user_info](#method-get_user_info)
      * [<kbd>method</kbd> reply](#method-reply-2)
      * [<kbd>method</kbd> send](#method-send-2)
      * [<kbd>method</kbd> send_group](#method-send_group-2)
* [<kbd>module</kbd> adapters.sop_bot.events](#module-adapterssop_botevents)
   * [<kbd>class</kbd> EventType](#class-eventtype)
   * [<kbd>class</kbd> Text](#class-text)
   * [<kbd>class</kbd> ChatMessage](#class-chatmessage)
   * [<kbd>class</kbd> EventSingleChat](#class-eventsinglechat)
   * [<kbd>class</kbd> EventNewSubscriber](#class-eventnewsubscriber)
   * [<kbd>class</kbd> EventURLVerification](#class-eventurlverification)
   * [<kbd>class</kbd> CallbackRequestBase](#class-callbackrequestbase)
   * [<kbd>class</kbd> CallbackRequest](#class-callbackrequest)
* [<kbd>module</kbd> adapter](#module-adapter)
   * [<kbd>class</kbd> BaseAdapter](#class-baseadapter)
      * [<kbd>method</kbd> __init__](#method-__init__)
      * [<kbd>method</kbd> extract_event](#method-extract_event)
      * [<kbd>method</kbd> get_response](#method-get_response)
      * [<kbd>method</kbd> reply](#method-reply)
      * [<kbd>method</kbd> send](#method-send)
      * [<kbd>method</kbd> send_group](#method-send_group)
* [<kbd>module</kbd> configs](#module-configs)
* [<kbd>module</kbd> configs.startup_config](#module-configsstartup_config)
   * [<strong>Global Variables</strong>](#global-variables-1)
   * [<kbd>class</kbd> DBConfig](#class-dbconfig)
   * [<kbd>class</kbd> RedisConfig](#class-redisconfig)
   * [<kbd>class</kbd> StartupConfig](#class-startupconfig)
* [<kbd>module</kbd> core](#module-core)
   * [<kbd>class</kbd> BaseBot](#class-basebot)
      * [<kbd>method</kbd> __init__](#method-__init__-4)
      * [<kbd>method</kbd> get_app](#method-get_app)
      * [<kbd>method</kbd> on_event](#method-on_event)
      * [<kbd>method</kbd> register_adapter](#method-register_adapter)
      * [<kbd>method</kbd> run](#method-run)
   * [<kbd>class</kbd> CSBot](#class-csbot)
      * [<kbd>method</kbd> __init__](#method-__init__-5)
         * [<kbd>property</kbd> lifecycle](#property-lifecycle)
         * [<kbd>property</kbd> scheduler](#property-scheduler)
      * [<kbd>method</kbd> get_app](#method-get_app-1)
      * [<kbd>method</kbd> get_fsm](#method-get_fsm)
      * [<kbd>method</kbd> on_event](#method-on_event-1)
      * [<kbd>method</kbd> register_adapter](#method-register_adapter-1)
      * [<kbd>method</kbd> register_fsm](#method-register_fsm)
      * [<kbd>method</kbd> reply](#method-reply-3)
      * [<kbd>method</kbd> run](#method-run-1)
      * [<kbd>method</kbd> send](#method-send-3)
      * [<kbd>method</kbd> send_group](#method-send_group-3)
      * [<kbd>method</kbd> webhook](#method-webhook)
* [<kbd>module</kbd> hooks](#module-hooks)
* [<kbd>module</kbd> hooks.bot_lifecycle](#module-hooksbot_lifecycle)
   * [<kbd>class</kbd> BotLifecycle](#class-botlifecycle)
      * [<kbd>method</kbd> __init__](#method-__init__-6)
      * [<kbd>method</kbd> emit_startup](#method-emit_startup)
      * [<kbd>method</kbd> on_startup](#method-on_startup)
* [<kbd>module</kbd> hooks.matcher](#module-hooksmatcher)
   * [<kbd>class</kbd> Matcher](#class-matcher)
      * [<kbd>method</kbd> __init__](#method-__init__-7)
      * [<kbd>method</kbd> process](#method-process)
      * [<kbd>method</kbd> test](#method-test)
* [<kbd>module</kbd> libs](#module-libs)
* [<kbd>module</kbd> libs.seatalk_openapi](#module-libsseatalk_openapi)
* [<kbd>module</kbd> libs.seatalk_openapi.client](#module-libsseatalk_openapiclient)
   * [<strong>Global Variables</strong>](#global-variables-2)
   * [<kbd>class</kbd> API](#class-api)
      * [<kbd>method</kbd> __init__](#method-__init__-8)
   * [<kbd>class</kbd> Employee](#class-employee)
   * [<kbd>class</kbd> ContactProfiles](#class-contactprofiles)
   * [<kbd>class</kbd> ServiceNoticeAlert](#class-servicenoticealert)
   * [<kbd>class</kbd> ServiceNoticeButton](#class-servicenoticebutton)
   * [<kbd>class</kbd> ServiceNoticeMessage](#class-servicenoticemessage)
   * [<kbd>class</kbd> SeaTalkOpenAPIClient](#class-seatalkopenapiclient)
      * [<kbd>method</kbd> __init__](#method-__init__-9)
      * [<kbd>method</kbd> get_access_token](#method-get_access_token)
      * [<kbd>method</kbd> get_contact_profile_v2](#method-get_contact_profile_v2)
      * [<kbd>method</kbd> get_employee_code_with_email](#method-get_employee_code_with_email)
      * [<kbd>method</kbd> refresh_access_token](#method-refresh_access_token)
      * [<kbd>method</kbd> request](#method-request)
      * [<kbd>method</kbd> send_group_chat_message](#method-send_group_chat_message)
      * [<kbd>method</kbd> send_service_notice](#method-send_service_notice)
      * [<kbd>method</kbd> send_single_chat_message](#method-send_single_chat_message)
* [<kbd>module</kbd> libs.seatalk_webhook](#module-libsseatalk_webhook)
* [<kbd>module</kbd> libs.seatalk_webhook.client](#module-libsseatalk_webhookclient)
   * [<kbd>class</kbd> WebhookMsgType](#class-webhookmsgtype)
   * [<kbd>class</kbd> WebhookClient](#class-webhookclient)
      * [<kbd>method</kbd> __init__](#method-__init__-10)
      * [<kbd>method</kbd> send](#method-send-4)
* [<kbd>module</kbd> log](#module-log)
* [<kbd>module</kbd> models](#module-models)
* [<kbd>module</kbd> models.config](#module-modelsconfig)
   * [<strong>Global Variables</strong>](#global-variables-4)
   * [<kbd>function</kbd> table_name](#function-table_name)
   * [<kbd>class</kbd> PluginConfig](#class-pluginconfig)
         * [<kbd>property</kbd> dirty_fields](#property-dirty_fields)
   * [<kbd>class</kbd> KVRecord](#class-kvrecord)
         * [<kbd>property</kbd> dirty_fields](#property-dirty_fields-1)
* [<kbd>module</kbd> models.database](#module-modelsdatabase)
   * [<kbd>function</kbd> get_db](#function-get_db)
* [<kbd>module</kbd> permissions](#module-permissions)
   * [<strong>Global Variables</strong>](#global-variables-5)
   * [<kbd>class</kbd> Permission](#class-permission)
      * [<kbd>method</kbd> __init__](#method-__init__-11)
      * [<kbd>method</kbd> allow](#method-allow)
* [<kbd>module</kbd> plugin](#module-plugin)
   * [<kbd>function</kbd> filter_matchers](#function-filter_matchers)
   * [<kbd>class</kbd> ConfigUpdateCallback](#class-configupdatecallback)
      * [<kbd>method</kbd> __init__](#method-__init__-12)
   * [<kbd>class</kbd> PluginLifecycle](#class-pluginlifecycle)
      * [<kbd>method</kbd> __init__](#method-__init__-13)
      * [<kbd>method</kbd> emit_config_updated](#method-emit_config_updated)
      * [<kbd>method</kbd> emit_on_load](#method-emit_on_load)
      * [<kbd>method</kbd> emit_on_unload](#method-emit_on_unload)
      * [<kbd>method</kbd> on_load](#method-on_load)
      * [<kbd>method</kbd> on_plugin_config_update](#method-on_plugin_config_update)
      * [<kbd>method</kbd> on_unload](#method-on_unload)
   * [<kbd>class</kbd> PluginAPI](#class-pluginapi)
      * [<kbd>method</kbd> __init__](#method-__init__-14)
   * [<kbd>class</kbd> Plugin](#class-plugin)
      * [<kbd>method</kbd> __init__](#method-__init__-15)
      * [<kbd>method</kbd> get_api_handler](#method-get_api_handler)
      * [<kbd>method</kbd> get_exported_func](#method-get_exported_func)
      * [<kbd>method</kbd> setup_auto_sync_lock](#method-setup_auto_sync_lock)
      * [<kbd>method</kbd> to_json](#method-to_json)
      * [<kbd>method</kbd> update_config](#method-update_config)
   * [<kbd>class</kbd> PluginManager](#class-pluginmanager)
      * [<kbd>classmethod</kbd> export](#classmethod-export)
      * [<kbd>classmethod</kbd> get_config](#classmethod-get_config)
      * [<kbd>classmethod</kbd> get_plugin_by_name](#classmethod-get_plugin_by_name)
      * [<kbd>classmethod</kbd> load_plugin](#classmethod-load_plugin)
      * [<kbd>classmethod</kbd> on_any](#classmethod-on_any)
      * [<kbd>classmethod</kbd> on_config_updated](#classmethod-on_config_updated)
      * [<kbd>classmethod</kbd> on_exact](#classmethod-on_exact)
      * [<kbd>classmethod</kbd> on_image](#classmethod-on_image)
      * [<kbd>classmethod</kbd> on_keyword](#classmethod-on_keyword)
      * [<kbd>classmethod</kbd> on_plugin_loaded](#classmethod-on_plugin_loaded)
      * [<kbd>classmethod</kbd> on_plugin_unloaded](#classmethod-on_plugin_unloaded)
      * [<kbd>classmethod</kbd> on_prefix](#classmethod-on_prefix)
      * [<kbd>classmethod</kbd> on_regex](#classmethod-on_regex)
      * [<kbd>classmethod</kbd> register_plugin_api](#classmethod-register_plugin_api)
* [<kbd>module</kbd> protocol](#module-protocol)
   * [<kbd>class</kbd> EventType](#class-eventtype-1)
   * [<kbd>class</kbd> MsgType](#class-msgtype)
   * [<kbd>class</kbd> ChannelType](#class-channeltype)
   * [<kbd>class</kbd> UserInfo](#class-userinfo)
   * [<kbd>class</kbd> GroupInfo](#class-groupinfo)
   * [<kbd>class</kbd> Message](#class-message)
      * [<kbd>method</kbd> __init__](#method-__init__-16)
   * [<kbd>class</kbd> QuoteMessage](#class-quotemessage)
   * [<kbd>class</kbd> EventChatMessage](#class-eventchatmessage)
   * [<kbd>class</kbd> EventNewSubscriber](#class-eventnewsubscriber-1)
   * [<kbd>class</kbd> CallbackMessage](#class-callbackmessage)
   * [<kbd>class</kbd> SendMessageRequest](#class-sendmessagerequest)
* [<kbd>module</kbd> role](#module-role)
   * [<kbd>class</kbd> BaseRole](#class-baserole)
      * [<kbd>method</kbd> __init__](#method-__init__-17)
      * [<kbd>classmethod</kbd> extract_from](#classmethod-extract_from)
      * [<kbd>method</kbd> is_developer](#method-is_developer)
      * [<kbd>method</kbd> is_owner](#method-is_owner)
   * [<kbd>class</kbd> Role](#class-role)
      * [<kbd>method</kbd> __init__](#method-__init__-18)
      * [<kbd>classmethod</kbd> extract_from](#classmethod-extract_from-1)
      * [<kbd>method</kbd> is_developer](#method-is_developer-1)
      * [<kbd>method</kbd> is_owner](#method-is_owner-1)
* [<kbd>module</kbd> rule](#module-rule)
   * [<kbd>function</kbd> rule_template](#function-rule_template)
   * [<kbd>function</kbd> rule_on_prefix](#function-rule_on_prefix)
   * [<kbd>function</kbd> rule_on_regex](#function-rule_on_regex)
   * [<kbd>function</kbd> rule_on_keyword](#function-rule_on_keyword)
   * [<kbd>function</kbd> rule_on_exact](#function-rule_on_exact)
* [<kbd>module</kbd> scheduler](#module-scheduler)
   * [<kbd>class</kbd> Scheduler](#class-scheduler)
      * [<kbd>method</kbd> __init__](#method-__init__-19)
         * [<kbd>property</kbd> idle_seconds](#property-idle_seconds)
         * [<kbd>property</kbd> next_run](#property-next_run)
         * [<kbd>property</kbd> pool](#property-pool)
      * [<kbd>method</kbd> every](#method-every)
      * [<kbd>method</kbd> run_pending](#method-run_pending)
   * [<kbd>class</kbd> Job](#class-job)
      * [<kbd>method</kbd> __init__](#method-__init__-20)
         * [<kbd>property</kbd> day](#property-day)
         * [<kbd>property</kbd> days](#property-days)
         * [<kbd>property</kbd> friday](#property-friday)
         * [<kbd>property</kbd> hour](#property-hour)
         * [<kbd>property</kbd> hours](#property-hours)
         * [<kbd>property</kbd> minute](#property-minute)
         * [<kbd>property</kbd> minutes](#property-minutes)
         * [<kbd>property</kbd> monday](#property-monday)
         * [<kbd>property</kbd> saturday](#property-saturday)
         * [<kbd>property</kbd> second](#property-second)
         * [<kbd>property</kbd> seconds](#property-seconds)
         * [<kbd>property</kbd> should_run](#property-should_run)
         * [<kbd>property</kbd> sunday](#property-sunday)
         * [<kbd>property</kbd> thursday](#property-thursday)
         * [<kbd>property</kbd> tuesday](#property-tuesday)
         * [<kbd>property</kbd> wednesday](#property-wednesday)
         * [<kbd>property</kbd> week](#property-week)
         * [<kbd>property</kbd> weeks](#property-weeks)
      * [<kbd>method</kbd> at](#method-at)
      * [<kbd>method</kbd> background_job_wrapper](#method-background_job_wrapper)
      * [<kbd>method</kbd> block_do](#method-block_do)
      * [<kbd>method</kbd> do](#method-do)
      * [<kbd>method</kbd> once](#method-once)
      * [<kbd>method</kbd> tag](#method-tag)
      * [<kbd>method</kbd> to](#method-to)
      * [<kbd>method</kbd> until](#method-until)
* [<kbd>module</kbd> session](#module-session)
   * [<kbd>class</kbd> State](#class-state)
   * [<kbd>class</kbd> FSM](#class-fsm)
      * [<kbd>method</kbd> __init__](#method-__init__-21)
      * [<kbd>method</kbd> clear_state](#method-clear_state)
      * [<kbd>method</kbd> get_state](#method-get_state)
      * [<kbd>method</kbd> handle_time_out](#method-handle_time_out)
      * [<kbd>method</kbd> maintain_states](#method-maintain_states)
      * [<kbd>method</kbd> remove_expired_states](#method-remove_expired_states)
      * [<kbd>method</kbd> state_key](#method-state_key)
      * [<kbd>method</kbd> store_state](#method-store_state)
   * [<kbd>class</kbd> BaseSession](#class-basesession)
      * [<kbd>method</kbd> __init__](#method-__init__-22)
         * [<kbd>property</kbd> aborted](#property-aborted)
         * [<kbd>property</kbd> event](#property-event)
         * [<kbd>property</kbd> state](#property-state)
      * [<kbd>method</kbd> abort](#method-abort)
      * [<kbd>method</kbd> stop](#method-stop)
   * [<kbd>class</kbd> MessageSession](#class-messagesession)
      * [<kbd>method</kbd> __init__](#method-__init__-23)
         * [<kbd>property</kbd> aborted](#property-aborted-1)
         * [<kbd>property</kbd> event](#property-event-1)
         * [<kbd>property</kbd> id](#property-id)
         * [<kbd>property</kbd> last_message_time](#property-last_message_time)
         * [<kbd>property</kbd> state](#property-state-1)
      * [<kbd>method</kbd> abort](#method-abort-1)
      * [<kbd>method</kbd> get_state](#method-get_state-1)
      * [<kbd>method</kbd> reply](#method-reply-4)
      * [<kbd>method</kbd> send](#method-send-5)
      * [<kbd>method</kbd> stop](#method-stop-1)
   * [<kbd>class</kbd> FriendListChangeSession](#class-friendlistchangesession)
      * [<kbd>method</kbd> __init__](#method-__init__-24)
         * [<kbd>property</kbd> aborted](#property-aborted-2)
         * [<kbd>property</kbd> event](#property-event-2)
         * [<kbd>property</kbd> state](#property-state-2)
      * [<kbd>method</kbd> abort](#method-abort-2)
      * [<kbd>method</kbd> stop](#method-stop-2)
   * [<kbd>class</kbd> SessionManager](#class-sessionmanager)
      * [<kbd>method</kbd> __init__](#method-__init__-25)
* [<kbd>module</kbd> store](#module-store)
   * [<strong>Global Variables</strong>](#global-variables-6)
   * [<kbd>class</kbd> ReconnectMySQLDatabase](#class-reconnectmysqldatabase)
   * [<kbd>class</kbd> Storage](#class-storage)
      * [<kbd>classmethod</kbd> delete](#classmethod-delete)
      * [<kbd>classmethod</kbd> get](#classmethod-get)
      * [<kbd>classmethod</kbd> init](#classmethod-init)
      * [<kbd>classmethod</kbd> init_migration](#classmethod-init_migration)
      * [<kbd>classmethod</kbd> range](#classmethod-range)
      * [<kbd>classmethod</kbd> set](#classmethod-set)
   * [<kbd>class</kbd> CacheManager](#class-cachemanager)
      * [<kbd>method</kbd> __init__](#method-__init__-26)


<a href="cs_bot/adapter.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `adapter`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/adapter.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseAdapter`




<a href="cs_bot/adapter.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'CSBot', config: Dict[str, Any])
```








---

<a href="cs_bot/adapter.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `extract_event`

```python
extract_event(
    raw_body: bytes,
    headers: Dict[str, str]
) → Optional[CallbackMessage]
```





---

<a href="cs_bot/adapter.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_response`

```python
get_response(raw_body: bytes, headers: Dict[str, str]) → Any
```





---

<a href="cs_bot/adapter.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reply`

```python
reply(event: EventChatMessage, message: Message, quote_reply: bool = False)
```





---

<a href="cs_bot/adapter.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(receiver_email: str, message: Message)
```





---

<a href="cs_bot/adapter.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_group`

```python
send_group(
    group_name: str,
    message: Message,
    mentioned_emails: Optional[List[str]] = None
)
```








<a href="cs_bot/adapters/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `adapters`








<a href="cs_bot/adapters/shopee_imbot/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `adapters.shopee_imbot`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ReceiveNewMessageRequest`
OnMessage callback request definition, used to deserialize the callback requests from the shopee_imbot callback server 





---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Adapter`
Adapter implement to adapt the shopee_imbot callback server 

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'CSBot', config: Dict[str, Any])
```








---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `encoded_content`

```python
encoded_content(message: Message)
```





---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `extract_event`

```python
extract_event(
    raw_body: bytes,
    headers: Dict[str, str]
) → Optional[CallbackMessage]
```

shopee-imbot has only one EventType: EventType.NEW_CHAT_MESSAGE :param raw_body: :param headers: :return: 

---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_response`

```python
get_response(raw_body: bytes, headers: Dict[str, str]) → Any
```





---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reply`

```python
reply(event: EventChatMessage, message: Message, quote_reply: bool = False)
```





---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(receiver_email: str, message: Message)
```





---

<a href="cs_bot/adapters/shopee_imbot/__init__.py#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_group`

```python
send_group(
    group_name: str,
    message: Message,
    mentioned_emails: Optional[List[str]] = None
)
```








<a href="cs_bot/adapters/sop_bot/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `adapters.sop_bot`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/adapters/sop_bot/__init__.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Adapter`




<a href="cs_bot/adapters/sop_bot/__init__.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'CSBot', config: Dict[str, Any])
```

Initialize the SOP Bot Adapter :param bot: CSBot instance :param config: StartupConfig.adapter 




---

<a href="cs_bot/adapters/sop_bot/__init__.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `extract_event`

```python
extract_event(
    raw_body: bytes,
    headers: Dict[str, str]
) → Optional[CallbackMessage]
```

https://open.seatalk.io/docs/messaging_messaging-events extract event from the callback request of the Seatalk Open Platform. :param raw_body: http body :param headers: http headers :rtype: protocol.CallbackMessage 

---

<a href="cs_bot/adapters/sop_bot/__init__.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_response`

```python
get_response(raw_body: bytes, headers: Dict[str, str]) → Any
```

:return: HTTP Response to return 

---

<a href="cs_bot/adapters/sop_bot/__init__.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_user_info`

```python
get_user_info(employee_codes: List[str]) → Dict[str, UserInfo]
```

get UserInfo by the employee_code :param employee_codes: employee_code of the Seatalk Open Platform :return: the respective user info 

---

<a href="cs_bot/adapters/sop_bot/__init__.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reply`

```python
reply(event: CallbackMessage, message: Message, quote_reply: bool = False)
```

Let the bot reply a message :param quote_reply: whether to quote the incoming message, not supported yet :param event: the origin event to reply :param message: the reply :return: None :raise: raise ValueError on invalid input message 

---

<a href="cs_bot/adapters/sop_bot/__init__.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(receiver_email: str, message: Message)
```

let the bot send a message :param receiver_email: email :param message: Message Instance :return: None :raise: raise ValueError on invalid input message 

---

<a href="cs_bot/adapters/sop_bot/__init__.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_group`

```python
send_group(
    group_name: str,
    message: Message,
    mentioned_emails: Optional[List[str]] = None
)
```








<a href="cs_bot/adapters/sop_bot/events.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `adapters.sop_bot.events`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/adapters/sop_bot/events.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventType`
EventType definition of the Event Callback from Seatalk Open Platform. See details in https://open.seatalk.io/docs/messaging_messaging-events . 





---

<a href="cs_bot/adapters/sop_bot/events.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Text`
TextMessage definition. See details in https://open.seatalk.io/docs/messaging_messaging-events . 





---

<a href="cs_bot/adapters/sop_bot/events.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ChatMessage`
Message definition. See details in https://open.seatalk.io/docs/messaging_messaging-events . 





---

<a href="cs_bot/adapters/sop_bot/events.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventSingleChat`
Event Definition of the Callback Event <message_from_bot_subscriber>. See details in https://open.seatalk.io/docs/messaging_messaging-events . 





---

<a href="cs_bot/adapters/sop_bot/events.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventNewSubscriber`
Event Definition of the Callback Event <new_bot_subscriber>. See details in https://open.seatalk.io/docs/messaging_messaging-events . 





---

<a href="cs_bot/adapters/sop_bot/events.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventURLVerification`
Event Definition of the Callback Event <event_verification>. See details in https://open.seatalk.io/docs/messaging_messaging-events . 





---

<a href="cs_bot/adapters/sop_bot/events.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CallbackRequestBase`
Common Fields of the Event Callback Request. See details in https://open.seatalk.io/docs/messaging_messaging-events . 





---

<a href="cs_bot/adapters/sop_bot/events.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CallbackRequest`
Event Callback Request definition See details in https://open.seatalk.io/docs/messaging_messaging-events . 







<a href="cs_bot/api_common.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `api_common`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

**Global Variables**
---------------
- **API_AUTH_KEY**

---

<a href="cs_bot/api_common.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `standard_response`

```python
standard_response(
    code: int = 0,
    error: Any = '',
    data: Any = None,
    status: int = 200
) → Response
```






---

<a href="cs_bot/api_common.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plugin_not_found`

```python
plugin_not_found(plugin_name: str) → Response
```






---

<a href="cs_bot/api_common.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plugin_not_enabled`

```python
plugin_not_enabled(plugin_name: str) → Response
```






---

<a href="cs_bot/api_common.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plugin_config_invalid`

```python
plugin_config_invalid(errors: Optional[List])
```






---

<a href="cs_bot/api_common.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plugin_api_not_found`

```python
plugin_api_not_found(plugin_name: str, api_path: str, method: str) → Response
```






---

<a href="cs_bot/api_common.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plugin_api_auth_required`

```python
plugin_api_auth_required(
    plugin_name: str,
    api_path: str,
    method: str
) → Response
```






---

<a href="cs_bot/api_common.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plugin_api_no_permission`

```python
plugin_api_no_permission(
    plugin_name: str,
    api_path: str,
    method: str,
    role_required: APIAuth
) → Response
```






---

<a href="cs_bot/api_common.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plugin_api_internal_error`

```python
plugin_api_internal_error(trace: str) → Response
```






---

<a href="cs_bot/api_common.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `APIAuth`
An enumeration. 





---

<a href="cs_bot/api_common.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AuthUser`




<a href="cs_bot/api_common.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(is_authenticated: bool, user: Optional[str], auth_role: APIAuth)
```











<a href="cs_bot/configs/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `configs`








<a href="cs_bot/configs/startup_config.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `configs.startup_config`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

**Global Variables**
---------------
- **DEFAULT_STARTUP_CONFIG**


---

<a href="cs_bot/configs/startup_config.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `DBConfig`
DBConfig address: address to the database  mysql:  TODO  sqlite: sqlite://path_to_your_db.db 

driver: "mysql" or "sqlite" are available 





---

<a href="cs_bot/configs/startup_config.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RedisConfig`
RedisConfig 





---

<a href="cs_bot/configs/startup_config.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `StartupConfig`
Startup Config definition of the CSBot 







<a href="cs_bot/core.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `core`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/core.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseBot`




<a href="cs_bot/core.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(config: Optional[StartupConfig] = None)
```








---

<a href="cs_bot/core.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_app`

```python
get_app()
```





---

<a href="cs_bot/core.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `on_event`

```python
on_event()
```





---

<a href="cs_bot/core.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `register_adapter`

```python
register_adapter(adapter: BaseAdapter)
```





---

<a href="cs_bot/core.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(host: str, port: int)
```

Runs the application on a local development server. :return: None 


---

<a href="cs_bot/core.py#L132"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CSBot`




<a href="cs_bot/core.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    config: Optional[StartupConfig] = StartupConfig(db=DBConfig(database='cs_bot.db', port=0, host='127.0.0.1', user='', password='', driver='sqlite', need_migration=False), redis=RedisConfig(host='127.0.0.1', port=6379, db=0), jwt_secret='', adapter={}, callback_path='/callback', signing_secret='', max_scheduler_workers=4, max_msg_handler_workers=32, owner_emails=[], developers=[], webhooks=[], debug=False)
)
```






---

#### <kbd>property</kbd> lifecycle





---

#### <kbd>property</kbd> scheduler







---

<a href="cs_bot/core.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_app`

```python
get_app()
```





---

<a href="cs_bot/core.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_fsm`

```python
get_fsm(key: Union[str, Type[ForwardRef('State')]]) → FSM
```





---

<a href="cs_bot/core.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `on_event`

```python
on_event()
```





---

<a href="cs_bot/core.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `register_adapter`

```python
register_adapter(adapter: BaseAdapter)
```





---

<a href="cs_bot/core.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `register_fsm`

```python
register_fsm(fsm_name: str, state_class: Type[ForwardRef('State')]) → FSM
```





---

<a href="cs_bot/core.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reply`

```python
reply(
    event: EventChatMessage,
    message: Union[str, Message],
    quote_reply: bool = False
)
```





---

<a href="cs_bot/core.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(host: str, port: int)
```

Runs the application on a local development server. :return: None 

---

<a href="cs_bot/core.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(receiver_email: Union[str, List[str]], message: Union[str, Message])
```





---

<a href="cs_bot/core.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_group`

```python
send_group(
    group_name: str,
    message: Union[str, Message],
    mentioned_emails: Optional[List[str]] = None
)
```





---

<a href="cs_bot/core.py#L210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `webhook`

```python
webhook(
    message: Union[str, bytes],
    msg_type: WebhookMsgType = <WebhookMsgType.TEXT: 'text'>
)
```








<a href="cs_bot/helper.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `helper`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 


---

<a href="cs_bot/helper.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `md5`

```python
md5(v: str) → str
```








<a href="cs_bot/hooks/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `hooks`








<a href="cs_bot/hooks/bot_lifecycle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `hooks.bot_lifecycle`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/hooks/bot_lifecycle.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BotLifecycle`
BotLifecycle 

<a href="cs_bot/hooks/bot_lifecycle.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

 






---

<a href="cs_bot/hooks/bot_lifecycle.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `emit_startup`

```python
emit_startup()
```

Emit the init event, iterate all the callback functions and call. :return: None 

---

<a href="cs_bot/hooks/bot_lifecycle.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `on_startup`

```python
on_startup() → Callable[[], Callable[, NoneType]]
```

on_init :return: a decorator to use to register an bot initialization callback :rtype: LifecycleHook_D 




<a href="cs_bot/hooks/matcher.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `hooks.matcher`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/hooks/matcher.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Matcher`
Base Matcher Definition A matcher has 3️ duties 1⃣️ To tell whether the session matches the rule. 2⃣️ To tell whether the session.role has permission to trigger the message process procedure. 3⃣️ Process the message. 

<a href="cs_bot/hooks/matcher.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    rule: Callable[[ForwardRef('Session')], bool],
    permission: Optional[Permission],
    priority: int,
    processor: Callable[[ForwardRef('MessageSession')], NoneType]
)
```

init a new matcher / message process procedure :param rule: A function to tell whether a matcher is matched with the input session. :param permission: Used to judge whether a session has the permission to trigger a specified matcher. :param priority: priority decides the execution order of all matched matchers. :param processor: the function to call to process the incoming session. 




---

<a href="cs_bot/hooks/matcher.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `process`

```python
process(session: MessageSession)
```

Process the incoming session, where the real logic should be set :param session: the incoming session :return: None 

---

<a href="cs_bot/hooks/matcher.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `test`

```python
test(session: MessageSession) → bool
```

tell whether the session match the current matcher :param session: the incoming session :return: True on matched otherwise False 




<a href="cs_bot/libs/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `libs`








<a href="cs_bot/libs/seatalk_openapi/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `libs.seatalk_openapi`








<a href="cs_bot/libs/seatalk_openapi/client.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `libs.seatalk_openapi.client`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

**Global Variables**
---------------
- **API_GET_ACCESS_TOKEN**
- **API_GET_CONTACT_PROFILE_V2**
- **API_SEND_SINGLE_CHAT**
- **API_GET_EMPLOYEE_CODE_WITH_EMAIL_V2**
- **API_SEND_SERVICE_NOTICE**
- **API_GET_DEPARTMENT_EMPLOYEES**
- **API_GET_DEPARTMENTS**
- **OK**
- **ACCESS_TOKEN_EXPIRED**
- **RATE_LIMIT**
- **SECRET_INVALID**


---

<a href="cs_bot/libs/seatalk_openapi/client.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `API`




<a href="cs_bot/libs/seatalk_openapi/client.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(path: str, method: str)
```









---

<a href="cs_bot/libs/seatalk_openapi/client.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Employee`








---

<a href="cs_bot/libs/seatalk_openapi/client.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ContactProfiles`








---

<a href="cs_bot/libs/seatalk_openapi/client.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ServiceNoticeAlert`








---

<a href="cs_bot/libs/seatalk_openapi/client.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ServiceNoticeButton`








---

<a href="cs_bot/libs/seatalk_openapi/client.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ServiceNoticeMessage`








---

<a href="cs_bot/libs/seatalk_openapi/client.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeaTalkOpenAPIClient`
Client implementation for the SeaTalk Open Platform Server API. See details in https://open.seatalk.io/docs/api-development-guide_ 

<a href="cs_bot/libs/seatalk_openapi/client.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(app_id: str, app_secret: str, company_key: str = '')
```








---

<a href="cs_bot/libs/seatalk_openapi/client.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_access_token`

```python
get_access_token()
```





---

<a href="cs_bot/libs/seatalk_openapi/client.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_contact_profile_v2`

```python
get_contact_profile_v2(employee_code_list: List[str]) → ContactProfiles
```

Use this API to obtain an employee's basic profile information. See details in https://open.seatalk.io/docs/get-employee-profile :param employee_code_list: a list of employee codes :return: ContactProfiles instance contains profiles of all the valid and scoped employees. 

---

<a href="cs_bot/libs/seatalk_openapi/client.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_employee_code_with_email`

```python
get_employee_code_with_email(emails: List[str]) → Dict[str, str]
```

Use this API to exchange a user's email for employee_code. Only employee whose status is in-position(2) would be returned by this method. See details in https://open.seatalk.io/docs/get-employee-code-with-email. :param emails: emails to exchange :return: A dict, email as the key and the respective employee_code as the value. 

---

<a href="cs_bot/libs/seatalk_openapi/client.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `refresh_access_token`

```python
refresh_access_token()
```

Get app access token, see details in https://open.seatalk.io/docs/get-app-access-token :return: None 

---

<a href="cs_bot/libs/seatalk_openapi/client.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `request`

```python
request(
    api: API,
    json: Dict = None,
    query: Dict = None,
    with_auth_header: bool = True
) → Dict
```





---

<a href="cs_bot/libs/seatalk_openapi/client.py#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_group_chat_message`

```python
send_group_chat_message(
    group_code: str,
    content: Union[str, bytes],
    content_type: str = 'text',
    mention_all: bool = False,
    mentioned_emails: Optional[List[str]] = None,
    mentioned_employee_codes: Optional[List[str]] = None
)
```





---

<a href="cs_bot/libs/seatalk_openapi/client.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_service_notice`

```python
send_service_notice(
    employee_codes: List[str],
    messages: Dict[str, ServiceNoticeMessage],
    default_language: str = ''
) → Dict[str, str]
```

See details in https://open.seatalk.io/docs/messaging_send-service-notice_i18n 

---

<a href="cs_bot/libs/seatalk_openapi/client.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_single_chat_message`

```python
send_single_chat_message(
    employee_code: str,
    content: Union[str, bytes],
    content_type: str = 'text'
)
```

Let the bot send a single chat message to its subscriber. See details in https://open.seatalk.io/docs/messaging_send-message-to-bot-subscriber_ :param employee_code: target employee_code :param content: message content :param content_type: "text" and the "markdown" are available :return: None 




<a href="cs_bot/libs/seatalk_webhook/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `libs.seatalk_webhook`








<a href="cs_bot/libs/seatalk_webhook/client.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `libs.seatalk_webhook.client`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/libs/seatalk_webhook/client.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `WebhookMsgType`
An enumeration. 





---

<a href="cs_bot/libs/seatalk_webhook/client.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `WebhookClient`




<a href="cs_bot/libs/seatalk_webhook/client.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(webhooks: List[str])
```








---

<a href="cs_bot/libs/seatalk_webhook/client.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(
    message: Union[str, bytes],
    msg_type: WebhookMsgType = <WebhookMsgType.TEXT: 'text'>
)
```








<a href="cs_bot/log.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `log`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

**Global Variables**
---------------
- **logging**: # Copyright 2001-2019 by Vinay Sajip. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Vinay Sajip
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.




Failed to generate docs for module metrics: ValueError("Duplicated timeseries in CollectorRegistry: {'cs_bot_message_handled_sum', 'cs_bot_message_handled', 'cs_bot_message_handled_count', 'cs_bot_message_handled_bucket', 'cs_bot_message_handled_created'}")

<a href="cs_bot/models/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `models`








<a href="cs_bot/models/config.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `models.config`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

**Global Variables**
---------------
- **TABLE_NAME_MAPPING**

---

<a href="cs_bot/models/config.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `table_name`

```python
table_name(model_class: Type[Model])
```






---

<a href="cs_bot/models/config.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PluginConfig`





---

#### <kbd>property</kbd> dirty_fields








---

<a href="cs_bot/models/config.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `KVRecord`





---

#### <kbd>property</kbd> dirty_fields










<a href="cs_bot/models/database.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `models.database`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 


---

<a href="cs_bot/models/database.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_db`

```python
get_db() → DatabaseProxy
```








<a href="cs_bot/permissions.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `permissions`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

**Global Variables**
---------------
- **OWNER**
- **DEVELOPER**
- **ANYONE**


---

<a href="cs_bot/permissions.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Permission`
Permission is a rule to determined whether a message can trigger the specified Matcher. 

<a href="cs_bot/permissions.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(policy: Callable[[ForwardRef('Session')], bool])
```








---

<a href="cs_bot/permissions.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `allow`

```python
allow(session: MessageSession) → bool
```

this method would be called to test whether the session has the permission to trigger the Matcher procedure. :param session: the incoming session to be tested :return: a bool value indicate the session has the permission or not 




<a href="cs_bot/plugin.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `plugin`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 


---

<a href="cs_bot/plugin.py#L342"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `filter_matchers`

```python
filter_matchers(sess: MessageSession) → List[Matcher]
```






---

<a href="cs_bot/plugin.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ConfigUpdateCallback`




<a href="cs_bot/plugin.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    f: Callable[[Type[ForwardRef('Config')]], NoneType],
    immediate: bool = False
)
```









---

<a href="cs_bot/plugin.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PluginLifecycle`




<a href="cs_bot/plugin.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```








---

<a href="cs_bot/plugin.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `emit_config_updated`

```python
emit_config_updated(new, is_init: bool = False)
```





---

<a href="cs_bot/plugin.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `emit_on_load`

```python
emit_on_load()
```





---

<a href="cs_bot/plugin.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `emit_on_unload`

```python
emit_on_unload()
```





---

<a href="cs_bot/plugin.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `on_load`

```python
on_load() → Callable[[], Callable[, NoneType]]
```





---

<a href="cs_bot/plugin.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `on_plugin_config_update`

```python
on_plugin_config_update(
    immediate: bool = False
) → Callable[[Callable[[Type[ForwardRef('Config')]], NoneType]], Callable[[Type[ForwardRef('Config')]], NoneType]]
```





---

<a href="cs_bot/plugin.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `on_unload`

```python
on_unload() → Callable[[], Callable[, NoneType]]
```






---

<a href="cs_bot/plugin.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PluginAPI`




<a href="cs_bot/plugin.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(handler: Callable[, Any], auth_role: APIAuth)
```









---

<a href="cs_bot/plugin.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Plugin`




<a href="cs_bot/plugin.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    module: module,
    name: str,
    lifecycle: PluginLifecycle,
    custom_api: Dict[str, Dict[str, PluginAPI]],
    config_class: Optional[Type[ForwardRef('Config')]],
    config,
    config_auto_sync: bool,
    exported_functions: Dict[str, Callable[[], Any]]
)
```








---

<a href="cs_bot/plugin.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_api_handler`

```python
get_api_handler(api_path: str, method: str) → Optional[PluginAPI]
```





---

<a href="cs_bot/plugin.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_exported_func`

```python
get_exported_func(function_name: str) → Optional[Callable[[], Any]]
```





---

<a href="cs_bot/plugin.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setup_auto_sync_lock`

```python
setup_auto_sync_lock()
```





---

<a href="cs_bot/plugin.py#L132"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict
```





---

<a href="cs_bot/plugin.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_config`

```python
update_config(new_config: Dict) → None
```






---

<a href="cs_bot/plugin.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PluginManager`







---

<a href="cs_bot/plugin.py#L234"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `export`

```python
export(
    alias: Optional[str] = None
) → Callable[[Callable[[], Any]], Callable[[], Any]]
```





---

<a href="cs_bot/plugin.py#L255"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_config`

```python
get_config(plugin_name: str) → Optional[Type[ForwardRef('Config')]]
```





---

<a href="cs_bot/plugin.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_plugin_by_name`

```python
get_plugin_by_name(plugin_name: str) → Optional[Plugin]
```





---

<a href="cs_bot/plugin.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `load_plugin`

```python
load_plugin(module_path: str) → Optional[Plugin]
```





---

<a href="cs_bot/plugin.py#L224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_any`

```python
on_any(permission: Optional[Permission], priority: int)
```





---

<a href="cs_bot/plugin.py#L251"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_config_updated`

```python
on_config_updated(immediate: bool = False) → Callable[[Callable], Callable]
```





---

<a href="cs_bot/plugin.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_exact`

```python
on_exact(
    pattern: Union[str, List[str]],
    permission: Optional[Permission],
    priority: int
)
```





---

<a href="cs_bot/plugin.py#L214"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_image`

```python
on_image(permission: Optional[Permission], priority: int)
```





---

<a href="cs_bot/plugin.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_keyword`

```python
on_keyword(
    keyword: Union[str, List[str]],
    permission: Optional[Permission],
    priority: int
)
```





---

<a href="cs_bot/plugin.py#L243"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_plugin_loaded`

```python
on_plugin_loaded() → Callable[[Callable], Callable]
```





---

<a href="cs_bot/plugin.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_plugin_unloaded`

```python
on_plugin_unloaded() → Callable[[Callable], Callable]
```





---

<a href="cs_bot/plugin.py#L174"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_prefix`

```python
on_prefix(
    prefix: Union[str, List[str]],
    permission: Optional[Permission],
    priority
) → Callable[[Callable[[ForwardRef('MessageSession')], NoneType]], Callable[[ForwardRef('MessageSession')], NoneType]]
```





---

<a href="cs_bot/plugin.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `on_regex`

```python
on_regex(
    pattern: Union[str, List[str]],
    permission: Optional[Permission],
    priority: int
)
```





---

<a href="cs_bot/plugin.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `register_plugin_api`

```python
register_plugin_api(
    path: str,
    methods: List[str],
    auth_role: APIAuth = <APIAuth.Anonymous: 0>
) → Callable[[Callable[, Any]], Callable[, Any]]
```








<a href="cs_bot/protocol.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `protocol`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/protocol.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventType`
An enumeration. 





---

<a href="cs_bot/protocol.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MsgType`
An enumeration. 





---

<a href="cs_bot/protocol.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ChannelType`
An enumeration. 





---

<a href="cs_bot/protocol.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `UserInfo`








---

<a href="cs_bot/protocol.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GroupInfo`








---

<a href="cs_bot/protocol.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Message`




<a href="cs_bot/protocol.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    content: Union[str, bytes],
    msg_type: MsgType = <MsgType.TEXT: 'text'>,
    **kwargs
)
```









---

<a href="cs_bot/protocol.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `QuoteMessage`








---

<a href="cs_bot/protocol.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventChatMessage`
pass 





---

<a href="cs_bot/protocol.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventNewSubscriber`








---

<a href="cs_bot/protocol.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CallbackMessage`








---

<a href="cs_bot/protocol.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SendMessageRequest`










<a href="cs_bot/role.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `role`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/role.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseRole`




<a href="cs_bot/role.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'CSBot', user_info: UserInfo)
```








---

<a href="cs_bot/role.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `extract_from`

```python
extract_from(bot: 'CSBot', event: CallbackMessage)
```





---

<a href="cs_bot/role.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_developer`

```python
is_developer() → bool
```





---

<a href="cs_bot/role.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_owner`

```python
is_owner() → bool
```






---

<a href="cs_bot/role.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Role`




<a href="cs_bot/role.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'CSBot', user_info: UserInfo)
```








---

<a href="cs_bot/role.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `extract_from`

```python
extract_from(bot: 'CSBot', event: CallbackMessage)
```





---

<a href="cs_bot/role.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_developer`

```python
is_developer() → bool
```





---

<a href="cs_bot/role.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_owner`

```python
is_owner() → bool
```








<a href="cs_bot/rule.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rule`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 


---

<a href="cs_bot/rule.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rule_template`

```python
rule_template(
    word: Union[str, List[str]],
    f: Callable[[List[str], str], bool]
) → Callable[[ForwardRef('Session')], bool]
```






---

<a href="cs_bot/rule.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rule_on_prefix`

```python
rule_on_prefix(
    prefix: Union[str, List[str]]
) → Callable[[ForwardRef('Session')], bool]
```






---

<a href="cs_bot/rule.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rule_on_regex`

```python
rule_on_regex(
    regex: Union[str, List[str]]
) → Callable[[ForwardRef('Session')], bool]
```






---

<a href="cs_bot/rule.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rule_on_keyword`

```python
rule_on_keyword(
    keyword: Union[str, List[str]]
) → Callable[[ForwardRef('Session')], bool]
```






---

<a href="cs_bot/rule.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rule_on_exact`

```python
rule_on_exact(
    keyword: Union[str, List[str]]
) → Callable[[ForwardRef('Session')], bool]
```








<a href="cs_bot/scheduler.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `scheduler`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/scheduler.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Scheduler`




<a href="cs_bot/scheduler.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(background_workers: int = 16)
```






---

#### <kbd>property</kbd> idle_seconds

:return: Number of seconds until  :meth:`next_run <Scheduler.next_run>`  or None if no jobs are scheduled 

---

#### <kbd>property</kbd> next_run

Datetime when the next job should run. 

:return: A :class:`~datetime.datetime` object  or None if no jobs scheduled 

---

#### <kbd>property</kbd> pool







---

<a href="cs_bot/scheduler.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `every`

```python
every(interval: int = 1) → Job
```





---

<a href="cs_bot/scheduler.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run_pending`

```python
run_pending()
```






---

<a href="cs_bot/scheduler.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Job`




<a href="cs_bot/scheduler.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(interval: int, scheduler: Scheduler = None)
```






---

#### <kbd>property</kbd> day





---

#### <kbd>property</kbd> days





---

#### <kbd>property</kbd> friday





---

#### <kbd>property</kbd> hour





---

#### <kbd>property</kbd> hours





---

#### <kbd>property</kbd> minute





---

#### <kbd>property</kbd> minutes





---

#### <kbd>property</kbd> monday





---

#### <kbd>property</kbd> saturday





---

#### <kbd>property</kbd> second





---

#### <kbd>property</kbd> seconds





---

#### <kbd>property</kbd> should_run

:return: ``True`` if the job should be run now. 

---

#### <kbd>property</kbd> sunday





---

#### <kbd>property</kbd> thursday





---

#### <kbd>property</kbd> tuesday





---

#### <kbd>property</kbd> wednesday





---

#### <kbd>property</kbd> week





---

#### <kbd>property</kbd> weeks







---

<a href="cs_bot/scheduler.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `at`

```python
at(time_str)
```





---

<a href="cs_bot/scheduler.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `background_job_wrapper`

```python
background_job_wrapper(f: Callable) → Callable
```





---

<a href="cs_bot/scheduler.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `block_do`

```python
block_do(job_func: Callable, *args, **kwargs)
```





---

<a href="cs_bot/scheduler.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `do`

```python
do(job_func: Callable, *args, **kwargs)
```





---

<a href="cs_bot/scheduler.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `once`

```python
once(job_func: Callable, *args, **kwargs)
```





---

<a href="cs_bot/scheduler.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `tag`

```python
tag(*tags: Hashable)
```





---

<a href="cs_bot/scheduler.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to`

```python
to(latest: int)
```





---

<a href="cs_bot/scheduler.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `until`

```python
until(until_time: Union[datetime, timedelta, time, str])
```








<a href="cs_bot/session.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `session`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 



---

<a href="cs_bot/session.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `State`
An enumeration. 





---

<a href="cs_bot/session.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `FSM`




<a href="cs_bot/session.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'CSBot', fsm_name: str, state_class: Type[ForwardRef('State')])
```








---

<a href="cs_bot/session.py#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clear_state`

```python
clear_state(customer_email: str) → Tuple[Optional[State], bool]
```

Reset the state to the default_state for the specified user :param customer_email: email :return: Tuple (previous_state, removed or not) 

---

<a href="cs_bot/session.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_state`

```python
get_state(custom_email: str) → <enum 'State'>
```





---

<a href="cs_bot/session.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `handle_time_out`

```python
handle_time_out() → Callable[[Callable[[str, ForwardRef('State')], Optional[Tuple[ForwardRef('State'), int]]]], Callable[[str, ForwardRef('State')], Optional[Tuple[ForwardRef('State'), int]]]]
```





---

<a href="cs_bot/session.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `maintain_states`

```python
maintain_states()
```





---

<a href="cs_bot/session.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `remove_expired_states`

```python
remove_expired_states() → Iterable[Tuple[str, State]]
```

Remove all the timeout states from the ZSET and trigger the FSM timeout handler. :return: an Iterable object of Tuple (email: str, previous_state: State) 

---

<a href="cs_bot/session.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `state_key`

```python
state_key(email: str) → str
```





---

<a href="cs_bot/session.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `store_state`

```python
store_state(customer_email: str, state: State, timeout: int)
```






---

<a href="cs_bot/session.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseSession`




<a href="cs_bot/session.py#L141"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    bot: 'CSBot',
    event: CallbackMessage,
    session_manager: 'SessionManager'
)
```






---

#### <kbd>property</kbd> aborted





---

#### <kbd>property</kbd> event





---

#### <kbd>property</kbd> state







---

<a href="cs_bot/session.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `abort`

```python
abort()
```





---

<a href="cs_bot/session.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop()
```






---

<a href="cs_bot/session.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MessageSession`




<a href="cs_bot/session.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    bot: 'CSBot',
    event: CallbackMessage,
    session_manager: 'SessionManager'
)
```






---

#### <kbd>property</kbd> aborted





---

#### <kbd>property</kbd> event





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> last_message_time





---

#### <kbd>property</kbd> state







---

<a href="cs_bot/session.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `abort`

```python
abort()
```





---

<a href="cs_bot/session.py#L193"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_state`

```python
get_state(state_class: Union[Type[ForwardRef('State')], str]) → State
```





---

<a href="cs_bot/session.py#L183"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reply`

```python
reply(message: Union[str, Message], quote_reply: bool = False)
```





---

<a href="cs_bot/session.py#L179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(receiver_email: Union[str, List[str]], message: Union[str, Message])
```





---

<a href="cs_bot/session.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop()
```






---

<a href="cs_bot/session.py#L214"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `FriendListChangeSession`




<a href="cs_bot/session.py#L215"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'CSBot', cm: CallbackMessage, session_manager: 'SessionManager')
```






---

#### <kbd>property</kbd> aborted





---

#### <kbd>property</kbd> event





---

#### <kbd>property</kbd> state







---

<a href="cs_bot/session.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `abort`

```python
abort()
```





---

<a href="cs_bot/session.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop()
```






---

<a href="cs_bot/session.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SessionManager`




<a href="cs_bot/session.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(cache_manager: CacheManager)
```











<a href="cs_bot/store.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `store`
Copyright 2022 SeaTalk Open Platform 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

https://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

**Global Variables**
---------------
- **TABLE_NAME_MAPPING**


---

<a href="cs_bot/store.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ReconnectMySQLDatabase`








---

<a href="cs_bot/store.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Storage`







---

<a href="cs_bot/store.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `delete`

```python
delete(key: str) → bool
```





---

<a href="cs_bot/store.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get`

```python
get(key: str) → Optional[str]
```





---

<a href="cs_bot/store.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `init`

```python
init(config: DBConfig)
```





---

<a href="cs_bot/store.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `init_migration`

```python
init_migration()
```





---

<a href="cs_bot/store.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `range`

```python
range(
    start_key: str,
    end_key: str,
    include_start_key: bool = True,
    include_end_key: bool = True
) → Iterable[Tuple[str, str]]
```





---

<a href="cs_bot/store.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `set`

```python
set(key: str, value: str)
```










