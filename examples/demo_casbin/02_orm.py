#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 20:06
# @Author  : CoderCharm
# @File    : casbin_orm.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
https://github.com/pycasbin/sqlalchemy-adapter/blob/master/README.md

pip install casbin_sqlalchemy_adapter

"""

import casbin
import casbin_sqlalchemy_adapter

adapter = casbin_sqlalchemy_adapter.Adapter('sqlite:///test.db')

e = casbin.Enforcer('./model.conf', adapter, True)

sub = "nick"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

# 添加
# res = e.add_policy("alice", "data1", "read")
# res = e.remove_policy("alice", "data1", "read")
print(res)

# if e.enforce(sub, obj, act):
#     # permit alice to read data1casbin_sqlalchemy_adapter
#     print("通过")
# else:
#     # deny the request, show an error
#     print("拒绝")

