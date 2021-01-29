#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 20:23
# @Author  : CoderCharm
# @File    : sys_casbin.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

casbin 权限

"""

import casbin
# from casbin import util
import casbin_sqlalchemy_adapter

from db.session import engine
from core.config import settings


def get_casbin() -> casbin.Enforcer:
    adapter = casbin_sqlalchemy_adapter.Adapter(engine)

    e = casbin.Enforcer(settings.CASBIN_MODEL_PATH, adapter, True)
    # e.add_function("ParamsMatch", params_match_func)

    return e

# def params_match(full_name_k1: str, key2: str):
#     """
#     去掉url ?后面的参数 只取路径
#     :param full_name_k1:
#     :param key2:
#     :return:
#     """
#     key1 = full_name_k1.split("?")[0]
#     return util.key_match2(key1, key2)
#
#
# def params_match_func(*args):
#     name1 = args[0]
#     name2 = args[1]
#     return params_match(name1, name2)
