#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:31
# @Author  : CoderCharm
# @File    : auth.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
纯增删改查操作，写在model里面
"""

from common.session import BaseModel, paginator
from peewee import CharField, IntegerField
# from playhouse.shortcuts import model_to_dict, dict_to_model


class User(BaseModel):
    """
    用户表
    """
    id = IntegerField()
    name = CharField()
    email = CharField()
    phone = IntegerField()
    username = CharField()
    avatar = CharField()
    password = CharField()

    class Meta:
        table_name = 'users'

    @classmethod
    def single_by_id(cls, uid: int):
        db = User.undelete().select(User.id, User.name, User.email, User.phone, User.username, User.avatar).\
            where(User.id == uid)
        return db.first()

    @classmethod
    def single_by_phone(cls, phone: int = 0):
        db = User.select()

        if phone != 0:
            db = db.where(User.phone == phone)
        return db.first()
        # if db:
        #     return model_to_dict(db)

    @classmethod
    def fetch_all(cls, page: int = 1, page_size: int = 10):
        db = User.undelete().select(User.name, User.email, User.phone, User.username, User.avatar, User.created_at,
                                    User.deleted_at)

        user_list, paginate = paginator(db, page, page_size, "id desc")

        return user_list, paginate


