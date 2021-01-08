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

"""
import random
import string

from db.session import SessionLocal
from api.v1.auth.schemas import user_schema
from api.v1.auth.crud.user import curd_user


def init_db(db: SessionLocal) -> None:
    nickname = input("输入昵称(直接回车随机生成):")
    email = input("输入邮箱(登录时使用):")
    password = input("输入密码:")

    if not nickname:
        nickname = "用户" + "".join(random.sample(string.digits, k=5))

    user_in = user_schema.UserCreate(
        nickname=nickname,
        email=email,
        password=password,
    )
    user = curd_user.create(db, obj_in=user_in)  # noqa: F841
    print(f"用户-{user.nickname}-创建成功")


db = SessionLocal()
init_db(db)
