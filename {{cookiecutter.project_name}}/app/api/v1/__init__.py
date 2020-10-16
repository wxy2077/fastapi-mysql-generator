#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 17:45
# @Author  : CoderCharm
# @File    : __init__.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

版本路由区分

# 可以在这里添加所需要的依赖
https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi

"""

from fastapi import APIRouter, Depends

from app.common.deps import check_jwt_token

from .auth.endpoints import router as auth_router
from .items.endpoints import router as items_router

api_v1_router = APIRouter()
api_v1_router.include_router(auth_router, prefix="/admin/auth", tags=["用户"])
api_v1_router.include_router(items_router, tags=["测试API"], dependencies=[Depends(check_jwt_token)])
