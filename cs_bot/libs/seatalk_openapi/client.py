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
import base64
import time
from threading import Lock
from typing import Dict, List, Union, Optional

import requests
from pydantic import BaseModel

from cs_bot.log import logger

# open APIs definition
_API_LIST = []


class API:
    def __init__(self, path: str, method: str):
        self.path: str = path
        self.method: str = method
        _API_LIST.append(self)


class Employee(BaseModel):
    employee_code: str
    seatalk_id: str
    seatalk_nickname: str
    avatar: str
    name: str
    email: str
    departments: List[str]
    gender: int
    mobile: str
    reporting_manager_employee_code: str


class ContactProfiles(BaseModel):
    employees: List[Employee]


class ServiceNoticeAlert(BaseModel):
    Label: str
    Level: int


class ServiceNoticeButton(BaseModel):
    link: Optional[str]
    label: Optional[str]


class ServiceNoticeMessage(BaseModel):
    title: str
    subtitle: str
    body: Optional[str]
    description: Optional[str]
    alert: Optional[ServiceNoticeAlert]
    button: Optional[ServiceNoticeButton]


API_GET_ACCESS_TOKEN = API("/auth/app_access_token", "post")
API_GET_CONTACT_PROFILE_V2 = API("/contacts/v2/profile", "get")
API_SEND_SINGLE_CHAT = API("/messaging/v2/single_chat", "post")
API_GET_EMPLOYEE_CODE_WITH_EMAIL_V2 = API("/contacts/v2/get_employee_code_with_email", "post")
API_SEND_SERVICE_NOTICE = API("/messaging/v2/service_notice/i18n", "post")
API_GET_DEPARTMENT_EMPLOYEES = API("/contacts/v2/department/employees", "get")
API_GET_DEPARTMENTS = API("/contacts/v2/departments", "get")

OK = 0
ACCESS_TOKEN_EXPIRED = 100
RATE_LIMIT = 101
SECRET_INVALID = 1000


class SeaTalkOpenAPIClient:
    """
    Client implementation for the SeaTalk Open Platform Server API.
    See details in https://open.seatalk.io/docs/api-development-guide_
    """
    __OPENAPI_HOST = "openapi.seatalk.io"

    def __init__(self, app_id: str, app_secret: str, company_key: str = ""):
        self.__lock = Lock()
        self.app_id: str = app_id
        self.app_secret: str = app_secret
        self.access_token: str = ""
        self.access_token_expire: int = 0

    def request(self, api: API, json: Dict = None, query: Dict = None, with_auth_header: bool = True) -> Dict:
        if with_auth_header:
            headers: Dict = {"Authorization": f"Bearer {self.get_access_token()}"}
        else:
            headers = {}
        url = f"https://{self.__OPENAPI_HOST}{api.path}"
        res = requests.request(api.method, url,
                               params=query, json=json, headers=headers, timeout=10)
        logger.info(
            f"[SeaTalk OpenAPI] url: {url}, query: {query}, json: {json}, "
            f"status_code: {res.status_code}, response: {res.text}"
        )
        if res.status_code != 200:
            raise ValueError(f"open API HTTP status error [{res.status_code}] rid: [{res.headers.get('x-rid', '')}]")
        else:
            data: Dict = res.json()
            code = data.get("code", None)
            if code == OK:
                return data
            elif code == ACCESS_TOKEN_EXPIRED:
                self.refresh_access_token()
                return self.request(api, json, query)
            else:
                raise ValueError(f"openapi code error: [{code}]")

    def get_access_token(self):
        if self.access_token == "" or self.access_token_expire - int(time.time()) < 10:
            with self.__lock:
                if self.access_token == "" or self.access_token_expire - int(time.time()) < 10:
                    self.refresh_access_token()
        return self.access_token

    def refresh_access_token(self):
        """
        Get app access token, see details in https://open.seatalk.io/docs/get-app-access-token
        :return: None
        """
        res = self.request(
            API_GET_ACCESS_TOKEN,
            json={"app_id": self.app_id, "app_secret": self.app_secret},
            with_auth_header=False
        )
        self.access_token = res.get("app_access_token")
        self.access_token_expire = int(time.time()) + res.get("expire")

    def get_contact_profile_v2(self, employee_code_list: List[str]) -> ContactProfiles:
        """
        Use this API to obtain an employee's basic profile information.
        See details in https://open.seatalk.io/docs/get-employee-profile
        :param employee_code_list: a list of employee codes
        :return: ContactProfiles instance contains profiles of all the valid and scoped employees.
        """
        res = self.request(API_GET_CONTACT_PROFILE_V2, query={"employee_code": ",".join(employee_code_list)})
        return ContactProfiles(**res)

    def get_employee_code_with_email(self, emails: List[str]) -> Dict[str, str]:
        """

        Use this API to exchange a user's email for employee_code.
        Only employee whose status is in-position(2) would be returned by this method.
        See details in https://open.seatalk.io/docs/get-employee-code-with-email.
        :param emails: emails to exchange
        :return: A dict, email as the key and the respective employee_code as the value.
        """
        email_employee_code_mapping = {}
        batch_size = 400

        for i in range(0, len(emails), batch_size):
            batch = emails[i: i + batch_size]
            if not batch:
                break

            res = self.request(API_GET_EMPLOYEE_CODE_WITH_EMAIL_V2, json={"emails": batch})

            for e in res.get("employees", []):
                if e.get("code", -1) == 0 and e.get("employee_status", 0) == 2:
                    email_employee_code_mapping[e.get("email")] = e.get("employee_code")
        return email_employee_code_mapping

    @staticmethod
    def __assemble_chat_message(content: Union[str, bytes], content_type: str = "text"):
        valid_content_types = {"text", "image", "markdown"}
        if content_type not in valid_content_types:
            raise ValueError(f"content type should be in one of the {valid_content_types}")

        message = {"tag": content_type}
        if content_type == "image" and isinstance(content, (str, bytes)):
            message["image"] = {
                "content": base64.b64encode(content).decode("latin-1")
            }
        elif content_type in {"text", "markdown"} and isinstance(content, str):
            message[content_type] = {
                "content": content
            }
        else:
            raise ValueError(f"invalid content type of {type(content)} for the {content_type} message")
        return message

    def send_single_chat_message(self, employee_code: str, content: Union[str, bytes], content_type: str = "text"):
        """
        Let the bot send a single chat message to its subscriber.
        See details in https://open.seatalk.io/docs/messaging_send-message-to-bot-subscriber_
        :param employee_code: target employee_code
        :param content: message content
        :param content_type: "text" and the "markdown" are available
        :return: None
        """
        message = self.__assemble_chat_message(content, content_type)
        self.request(API_SEND_SINGLE_CHAT, json={"employee_code": employee_code, "message": message})

    def send_group_chat_message(self, group_code: str, content: Union[str, bytes], content_type: str = "text",
                                mention_all: bool = False,
                                mentioned_emails: Optional[List[str]] = None,
                                mentioned_employee_codes: Optional[List[str]] = None):

        raise NotImplementedError()

    def send_service_notice(self, employee_codes: List[str], messages: Dict[str, ServiceNoticeMessage],
                            default_language: str = "") -> Dict[str, str]:
        """
        See details in https://open.seatalk.io/docs/messaging_send-service-notice_i18n
        """
        if len(messages) == 0:
            raise ValueError("send_service_notice API require at least one message")
        if default_language not in messages:
            default_language = list(messages.keys())[0]
        language_messages_map: Dict[str, Dict] = {}
        for language, message in messages.items():
            if not (0 < len(message.title) < 60):
                raise ValueError(f"title length should be in [1, 59] got {len(message.title)} instead")
            if not (0 < len(message.subtitle) < 1000):
                raise ValueError(f"subtitle length should be in [1, 999] got {len(message.subtitle)} instead")
            language_messages_map[language] = message.dict()

        error_reasons_map = {}
        batch_size = 100
        for i in range(0, len(employee_codes), batch_size):
            batch = employee_codes[i: i + batch_size]
            if not batch:
                break

            res = self.request(
                API_SEND_SERVICE_NOTICE,
                json={"default_language": default_language, "messages": language_messages_map, "employee_codes": batch}
            )
            error_reasons_map.update({
                batch[offset]: reason
                for offset, reason in zip(res.get("failed_offsets", []), res.get("failed_reasons", []))
            })
        return error_reasons_map
