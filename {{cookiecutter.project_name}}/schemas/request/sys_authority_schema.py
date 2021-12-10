#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 19:40
# @Author  : CoderCharm
# @File    : sys_authority_schema.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

角色的校验规则

"""
from pydantic import BaseModel


# 角色创建
class AuthorityCreate(BaseModel):
    authority_id: int
    authority_name: str
    parent_id: int


# 修改角色(只允许修改角色名)
class AuthorityUpdate(BaseModel):
    authority_name: str
