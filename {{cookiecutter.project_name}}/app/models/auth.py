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
from app.db.base_class import Base, gen_uuid


class AdminUser(Base):
    """
    管理员表
    """
    __tablename__ = "admin_user"
    user_id = Column(VARCHAR(32), default=gen_uuid, unique=True, comment="用户id")
    email = Column(VARCHAR(128), unique=True, index=True, nullable=False, comment="邮箱")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    nickname = Column(VARCHAR(128), comment="管理员昵称")
    avatar = Column(VARCHAR(256), comment="管理员头像")
    hashed_password = Column(VARCHAR(128), nullable=False, comment="密码")
    is_active = Column(Integer, default=False, comment="邮箱是否激活 0=未激活 1=激活", server_default="0")
    role_id = Column(Integer, comment="角色表")
    __table_args__ = ({'comment': '管理员表'})
