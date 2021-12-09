#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 20:30
# @Author  : CoderCharm
# @File    : sys_casbin.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
校验casbin
"""

from pydantic import BaseModel


# 创建API
class AuthCreate(BaseModel):
    authority_id: str
    path: str
    method: str
