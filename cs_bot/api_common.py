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
import json
from enum import Enum
from typing import Callable, Any, Optional, List

from flask import Response

API_AUTH_KEY = "authorization"


class APIAuth(Enum):
    Anonymous = 0
    Admin = 1
    User = 2


class AuthUser:
    def __init__(self, is_authenticated: bool, user: Optional[str], auth_role: APIAuth):
        self.is_authenticated: bool = is_authenticated
        self.user: Optional[str] = user
        self.role: APIAuth = auth_role


def standard_response(code: int = 0, error: Any = "", data: Any = None, status: int = 200) -> Response:
    return Response(json.dumps({"code": code, "error": error, "data": data}), status=status)


def plugin_not_found(plugin_name: str) -> Response:
    return standard_response(error=f"plugin [{plugin_name}] is not registered", status=404)


def plugin_not_enabled(plugin_name: str) -> Response:
    return standard_response(error=f"plugin [{plugin_name}] is disabled", status=404)


def plugin_config_invalid(errors: Optional[List]):
    return standard_response(
        error=errors,
        status=400
    )


def plugin_api_not_found(plugin_name: str, api_path: str, method: str) -> Response:
    return standard_response(
        error=f"API [{method} /{api_path}] has not been registered by the plugin [{plugin_name}]",
        status=404
    )


def plugin_api_auth_required(plugin_name: str, api_path: str, method: str) -> Response:
    return standard_response(
        error=f"API [{method} {plugin_name}/{api_path}] requires authentication",
        status=401
    )


def plugin_api_no_permission(plugin_name: str, api_path: str, method: str, role_required: APIAuth) -> Response:
    return standard_response(
        error=f"API [{method} {plugin_name}/{api_path}] requires the role {role_required.name}",
        status=403
    )


def plugin_api_internal_error(trace: str) -> Response:
    return standard_response(
        error=" ".join(["internal error", trace]),
        status=404
    )
