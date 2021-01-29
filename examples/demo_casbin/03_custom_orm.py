#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 20:49
# @Author  : CoderCharm
# @File    : casbin_custom_orm.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

加一个自定义的解析函数

"""

import casbin
from casbin import util
import casbin_sqlalchemy_adapter

adapter = casbin_sqlalchemy_adapter.Adapter('sqlite:///test.db')

e = casbin.Enforcer('./custom_model.conf', adapter, True)


# 添加
# e.add_policy("999", "/api/user", "GET")
# 删除
# e.remove_policy("999", "/api/user", "GET")


def params_match(full_name_k1: str, key2: str):
    """
    去掉url ?后面的参数 只取路径
    :param full_name_k1:
    :param key2:
    :return:
    """
    key1 = full_name_k1.split("?")[0]
    return util.key_match2(key1, key2)


def params_match_func(*args):
    name1 = args[0]
    name2 = args[1]
    return params_match(name1, name2)


e.add_function("ParamsMatch", params_match_func)

sub = "999"  # the user that wants to access a resource.
obj = "/api/user?aaa=1"  # the resource that is going to be accessed.
act = "GET"  # the operation that the user performs on the resource.

if e.enforce(sub, obj, act):
    # permit alice to read data1casbin_sqlalchemy_adapter
    print("通过")
else:
    # deny the request, show an error
    print("拒绝")
