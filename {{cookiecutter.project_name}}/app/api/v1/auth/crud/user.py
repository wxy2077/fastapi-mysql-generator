#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:41
# @Author  : CoderCharm
# @File    : user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
管理员用户表的CRUD
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.common.curd_base import CRUDBase
from app.models.auth import AdminUser
from ..schemas import user_schema


class CRUDUser(CRUDBase[AdminUser, user_schema.UserCreate, user_schema.UserUpdate]):

    @staticmethod
    def get_by_email(db: Session, *, email: str) -> Optional[AdminUser]:
        """
        通过email获取用户
        参数里面的* 表示 后面调用的时候 要用指定参数的方法调用
        正确调用方式
            curd_user.get_by_email(db, email="xxx")
        错误调用方式
            curd_user.get_by_email(db, "xxx")
        :param db:
        :param email:
        :return:
        """
        return db.query(AdminUser).filter(AdminUser.email == email).first()

    def create(self, db: Session, *, obj_in: user_schema.UserCreate) -> AdminUser:
        db_obj = AdminUser(
            nickname=obj_in.nickname,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            avatar=obj_in.avatar,
            role_id=obj_in.role_id,
            is_active=obj_in.is_active
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[AdminUser]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def is_active(user: AdminUser) -> bool:
        return user.is_active == 1


curd_user = CRUDUser(AdminUser)
