#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:38
# @Author  : CoderCharm
# @File    : user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from typing import Any
from datetime import timedelta

from fastapi import APIRouter, Depends

from core import security
from models.users import User
from common import deps, logger
from schemas.response import resp
from core.config import settings
from schemas.request import sys_user_schema
from playhouse.shortcuts import model_to_dict

from logic.user_logic import UserLogic

router = APIRouter()


@router.post("/login", summary="用户登录认证", name="登录")
def login_access_token(
        *,
        req: sys_user_schema.UserPhoneAuth,
) -> Any:
    """
    简单实现登录
    :param req:
    :return:
    """

    # 验证用户 简短的业务可以写在这里
    # user = User.single_by_phone(phone=req.username)
    # if not user:
    #     return resp.fail(resp.DataNotFound.set_msg("账号或密码错误"))
    #
    # if not security.verify_password(req.password, user.password):
    #     return resp.fail(resp.DataNotFound.set_msg("账号或密码错误"))
    #
    # access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    #
    # # 登录token 存储了user.id
    # return resp.ok(data={
    #     "token": security.create_access_token(user.id, expires_delta=access_token_expires),
    # })

    # 复杂的业务逻辑建议 抽离到 logic文件夹下
    token = UserLogic().user_login_logic(req.username, req.password)
    return resp.ok(data={"token": token})


@router.get("/user/info", summary="获取用户信息", name="获取用户信息", description="此API没有验证权限")
def get_user_info(
        *,
        current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    获取用户信息 这个路由分组没有验证权限
    :param current_user:
    :return:
    """
    return resp.ok(data=model_to_dict(current_user))
