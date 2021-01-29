#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 15:43
# @Author  : CoderCharm
# @File    : sys_api.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
API 增删改查操作
"""

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from common import deps
from schemas.request.sys_api import ApiCreate
from schemas.response import response_code
from service.sys_api import curd_api

router = APIRouter()


@router.get("/all/apis", summary="获取所有API", name="获取所有API", description="获取所有API")
async def get_all_apis(
        db: Session = Depends(deps.get_db),
):
    api_list = curd_api.get_multi(db)
    return response_code.resp_200(data=api_list)


@router.post("/add/api", summary="添加API", name="添加API", description="添加API")
async def add_api(
        api_info: ApiCreate,
        db: Session = Depends(deps.get_db),
):
    obj_info = curd_api.create(db, api_info)
    return response_code.resp_200(data=obj_info)
