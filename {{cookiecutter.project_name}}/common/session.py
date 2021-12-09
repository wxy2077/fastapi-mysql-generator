#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 11:42
# @Author  : CoderCharm
# @File    : session.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""
import math
import datetime

from peewee import _ConnectionState, Model, ModelSelect, SQL, DateTimeField
from contextvars import ContextVar
from playhouse.pool import PooledMySQLDatabase

# from core.config import settings

# db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state_default = {"closed": None, "conn": None, "ctx": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = PooledMySQLDatabase(
    "fastapi",
    max_connections=8,
    stale_timeout=300,
    user="root",
    host="127.0.0.1",
    password="123456",
    port=3306
)

db._state = PeeweeConnectionState()


class BaseModel(Model):
    deleted_at = DateTimeField()
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    @classmethod
    def public(cls):
        return cls.select().where(SQL("deleted_at is NULL"))

    class Meta:
        database = db


def paginator(db: ModelSelect, page: int, page_size: int, order_by: str = "id ASC"):
    """
    分页
    """
    count = db.count()
    if page < 1:
        page = 1

    if page_size <= 0:
        page_size = 10

    if page_size >= 100:
        page_size = 100

    if page == 1:
        offset = 0
    else:
        offset = (page - 1) * page_size

    db = db.offset(offset).limit(page_size).order_by(SQL(order_by))

    total_pages = math.ceil(count / page_size)

    paginator = {
        "total_pages": total_pages,
        "count": count,
        "current_page": page,
        "pre_page": page - 1 if page > 1 else page,
        "next_page": page if page == total_pages else page + 1
    }

    return list(db.dicts()), paginator

