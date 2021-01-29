#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 21:11
# @Author  : CoderCharm
# @File    : sys_api.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
path = Column(VARCHAR(128), comment="API路径")
description = Column(VARCHAR(64), comment="API描述")
api_group = Column(VARCHAR(32), comment="API分组")
method = Column(VARCHAR(16), comment="请求方法")
"""
from pydantic import BaseModel


# 创建API
class ApiCreate(BaseModel):
    path: str
    description: str
    api_group: str
    method: str


class UpdateApi(BaseModel):
    id: str


class DelApi(BaseModel):
    id: str
