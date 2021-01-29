#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 11:40
# @Author  : CoderCharm
# @File    : base.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
需要使用 alembic 生成表的 记得在这里 从models里面 倒入进来才行 否则不会生成
"""

# Import all the models, so that Base has them before being
# imported by Alembic

# imported by Alembic # 方便在Alembic导入,迁移用

from db.base_class import Base  # noqa
from models.sys_auth import SysUser, SysAuthorities
from models.sys_api import SysApi