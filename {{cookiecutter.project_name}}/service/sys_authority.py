#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 19:37
# @Author  : CoderCharm
# @File    : sys_authority.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

管理员角色的CRUD

"""

from sqlalchemy.orm import Session

from models.sys_auth import SysAuthorities
from schemas.request import sys_authority_schema
from service.curd_base import CRUDBase


class CRUDAuthorities(
    CRUDBase[SysAuthorities,
             sys_authority_schema.AuthorityCreate,
             sys_authority_schema.AuthorityUpdate]
):

    def create(self, db: Session, *, obj_in: sys_authority_schema.AuthorityCreate) -> SysAuthorities:
        """
        创建角色
        :param db:
        :param obj_in:
        :return:
        """
        db_obj = SysAuthorities(
            authority_id=obj_in.authority_id,
            authority_name=obj_in.authority_name,
            parent_id=obj_in.parent_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


curd_authority = CRUDAuthorities(SysAuthorities)
