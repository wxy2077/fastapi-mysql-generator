#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 11:51
# @Author  : CoderCharm
# @File    : deps.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

一些通用的依赖功能

"""
from typing import Any, Union, Optional
#
from jose import jwt
from fastapi import Header, Depends, Request
from pydantic import ValidationError

from common import custom_exc
from models.users import User
from core.config import settings


def check_jwt_token(
        token: Optional[str] = Header(..., description="登录token")
) -> Union[str, Any]:
    """
    解析验证token  默认验证headers里面为token字段的数据
    可以给 headers 里面token替换别名, 以下示例为 X-Token
    token: Optional[str] = Header(None, alias="X-Token")
    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise custom_exc.TokenExpired()
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exc.TokenAuthError()


def get_current_user(
        token: Optional[str] = Depends(check_jwt_token)
) -> User:
    """
    根据header中token 获取当前用户
    :param db:
    :param token:
    :return:
    """
    user = User.single_by_id(uid=token.get("sub"))
    if not user:
        raise custom_exc.TokenAuthError(err_desc="User not found")
    return user