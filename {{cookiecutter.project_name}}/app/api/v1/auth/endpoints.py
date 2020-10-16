#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:38
# @Author  : CoderCharm
# @File    : index.py
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

from app.core import security
from app.common import deps, response_code, logger
from app.models import auth
from app.core.config import settings

from .schemas import user_schema
from .crud.user import curd_user

router = APIRouter()


@router.post("/login/access-token", summary="用户登录认证")
async def login_access_token(
        *,
        db: Session = Depends(deps.get_db),
        user_info: user_schema.UserEmailAuth,
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

    # 登录token 只存放了user.id
    return response_code.resp_200(data={
        "token": security.create_access_token(user.id, expires_delta=access_token_expires),
    })


@router.get("/user/info", summary="获取用户信息")
async def get_user_info(
        *,
        current_user: auth.AdminUser = Depends(deps.get_current_user)
) -> Any:
    """
    获取用户信息
    :param current_user:
    :return:
    """
    return response_code.resp_200(data={
        "nickname": current_user.nickname,
        "avatar": current_user.avatar
    })
