#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:38
# @Author  : CoderCharm
# @File    : sys_user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from typing import Any
from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from core import security
from models import sys_auth
from common import deps, logger
from core.config import settings
from schemas.request import sys_user_schema
from schemas.response import response_code
from service.sys_user import curd_user

router = APIRouter()


@router.post("/login/access-token", summary="用户登录认证", name="登录")
async def login_access_token(
        *,
        db: Session = Depends(deps.get_db),
        user_info: sys_user_schema.UserEmailAuth,
) -> Any:
    """
    用户JWT登录
    :param db:
    :param user_info:
    :return:
    """

    # 验证用户
    user = curd_user.authenticate(db, email=user_info.username, password=user_info.password)
    if not user:
        logger.info(f"用户邮箱认证错误: email{user_info.username} password:{user_info.password}")
        return response_code.resp_4003(message="username or password error")
    elif not curd_user.is_active(user):
        return response_code.resp_4003(message="User email not activated")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # 登录token 存储了user.id 和 authority_id
    return response_code.resp_200(data={
        "token": security.create_access_token(user.id, user.authority_id, expires_delta=access_token_expires),
    })


@router.get("/user/info", summary="获取用户信息", name="获取用户信息", description="此API没有验证权限")
async def get_user_info(
        *,
        current_user: sys_auth.SysUser = Depends(deps.get_current_user)
) -> Any:
    """
    获取用户信息 这个路由分组没有验证权限
    :param current_user:
    :return:
    """
    return response_code.resp_200(data={
        "nickname": current_user.nickname,
        "avatar": current_user.avatar
    })
