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

"""

from sqlalchemy import Column, Integer, VARCHAR
from db.base_class import Base, gen_uuid


class SysUser(Base):
    """
    用户表
    """
    user_id = Column(VARCHAR(32), default=gen_uuid, unique=True, comment="用户id")
    email = Column(VARCHAR(128), unique=True, index=True, nullable=False, comment="邮箱")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    nickname = Column(VARCHAR(128), comment="管理员昵称")
    avatar = Column(VARCHAR(256), comment="管理员头像")
    hashed_password = Column(VARCHAR(128), nullable=False, comment="密码")
    is_active = Column(Integer, default=False, comment="邮箱是否激活 0=未激活 1=激活", server_default="0")
    authority_id = Column(Integer, default=100, comment="角色id")
    __table_args__ = ({'comment': '系统用户表'})


class SysAuthorities(Base):
    """
    角色表
    """
    authority_id = Column(Integer, default=100, unique=True, comment="权限id")
    authority_name = Column(VARCHAR(32), comment="角色名")
    parent_id = Column(Integer,  nullable=True, unique=True, comment="父角色id")
    __table_args__ = ({'comment': '用户角色表'})




