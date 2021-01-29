#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 15:44
# @Author  : CoderCharm
# @File    : sys_api.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
API 的管理
"""

from sqlalchemy.orm import Session

from models.sys_api import SysApi
from schemas.request import sys_api
from service.curd_base import CRUDBase


class CRUDApi(
    CRUDBase[SysApi, sys_api.ApiCreate, sys_api.UpdateApi]
):

    def create(self, db: Session, *, obj_in: sys_api.ApiCreate) -> SysApi:
        """
        创建角色
        :param db:
        :param obj_in:
        :return:
        """
        db_obj = SysApi(
            path=obj_in.path,
            description=obj_in.description,
            api_group=obj_in.api_group,
            method=obj_in.method
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


curd_api = CRUDApi(SysApi)