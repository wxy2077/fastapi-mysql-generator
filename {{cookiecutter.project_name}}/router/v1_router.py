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

from fastapi import APIRouter
# from common.deps import check_authority

from api.v1.user import router as user_router
from api.v1.items import router as items_router
from api.v1.sys_scheduler import router as scheduler_router


api_v1_router = APIRouter()

# api_v1_router.include_router(items_router, tags=["测试API"], dependencies=[Depends(check_jwt_token)])
# check_authority 权限验证内部包含了 token 验证 如果不校验权限可直接 dependencies=[Depends(check_jwt_token)]
api_v1_router.include_router(items_router, tags=["测试接口"])
api_v1_router.include_router(user_router, prefix="/user", tags=["用户"])
api_v1_router.include_router(scheduler_router, tags=["任务调度"])
