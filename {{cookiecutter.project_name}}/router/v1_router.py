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

fastapi 没有像flask那样 分组子路由没有 middleware("http") 但是有 dependencies

"""

from fastapi import APIRouter, Depends
from common.deps import check_authority

from api.v1.sys_user import router as auth_router
from api.v1.items import router as items_router
from api.v1.sys_scheduler import router as scheduler_router
from api.v1.sys_api import router as sys_api_router
from api.v1.sys_casbin import router as sys_casbin_router


api_v1_router = APIRouter()
api_v1_router.include_router(auth_router, prefix="/admin/auth", tags=["用户"])

# api_v1_router.include_router(items_router, tags=["测试API"], dependencies=[Depends(check_jwt_token)])
# check_authority 权限验证内部包含了 token 验证 如果不校验权限可直接 dependencies=[Depends(check_jwt_token)]
api_v1_router.include_router(items_router, tags=["测试接口"], dependencies=[Depends(check_authority)])
api_v1_router.include_router(scheduler_router, tags=["任务调度"],  dependencies=[Depends(check_authority)])
api_v1_router.include_router(sys_api_router, tags=["服务API管理"],  dependencies=[Depends(check_authority)])
api_v1_router.include_router(sys_casbin_router, tags=["权限API管理"],  dependencies=[Depends(check_authority)])
