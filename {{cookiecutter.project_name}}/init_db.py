#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:33
# @Author  : CoderCharm
# @File    : create_user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
初始化数据库角色


"""

from db.session import SessionLocal
from schemas.request import sys_user_schema, sys_authority_schema
from service.sys_user import curd_user
from service.sys_authority import curd_authority
from common.sys_casbin import get_casbin
from router.v1_router import api_v1_router


def init_authority(db: SessionLocal) -> None:
    """
    创建角色
        999 为超级管理员用户
        100 为普通用户
    :param db:
    :return:
    """
    authority_info_list = [
        {"authority_id": 999, "authority_name": "超级管理员", "parent_id": 0},
        {"authority_id": 100, "authority_name": "普通用户", "parent_id": 999},
    ]

    for authority_info in authority_info_list:
        authority_in = sys_authority_schema.AuthorityCreate(
            authority_id=authority_info["authority_id"],
            authority_name=authority_info["authority_name"],
            parent_id=authority_info["parent_id"],
        )
        authority = curd_authority.create(db, obj_in=authority_in)  # noqa: F841
        print(f"角色-{authority.authority_name}-创建成功")


def init_user(db: SessionLocal) -> None:
    """
    创建基础的用户
    :param db:
    :return:
    """
    user_info_list = [
        {"nickname": "王小右", "email": "admin@admin.com", "password": "admin", "authority_id": 999,
         "avatar": "https://image.3001.net/images/20200504/1588558613_5eaf7b159c8e9.jpeg"},
        {"nickname": "测试用户", "email": "test@test.com", "password": "test", "authority_id": 100,
         "avatar": "https://image.3001.net/images/20200504/1588558613_5eaf7b159c8e9.jpeg"},
    ]
    for user_info in user_info_list:
        user_in = sys_user_schema.UserCreate(
            nickname=user_info["nickname"],
            email=user_info["email"],
            password=user_info["password"],
            authority_id=user_info["authority_id"],  # 权限id
            avatar=user_info["avatar"]
        )
        user = curd_user.create(db, obj_in=user_in)  # noqa: F841
        print(f"用户-{user.nickname}-创建成功")


def init_casbin():
    """
    初始化casbin的基本API数据

    把 api_v1_router 分组的所有路由都添加到 casbin里面
    :return:
    """
    e = get_casbin()

    for route in api_v1_router.routes:
        if route.name == "登录":
            # 登录不验证权限
            continue
        for method in route.methods:
            # 添加casbin规则
            e.add_policy("999", route.path, method)


db = SessionLocal()

init_authority(db)
init_user(db)
init_casbin()


