#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 20:36
# @Author  : CoderCharm
# @File    : sys_casbin.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
更新casbin权限

更多其他操作查看文档
https://casbin.org/docs/zh-CN/management-api
(目前文档好像没有更新Python示例 2021/1/29)

"""

from fastapi import APIRouter

from common.sys_casbin import get_casbin
from schemas.response import response_code
from schemas.request.sys_casbin import AuthCreate

router = APIRouter()


@router.post("/add/auth", summary="添加访问权限", name="添加访问权限", description="添加访问权限")
async def add_authority(
        authority_info: AuthCreate
):
    e = get_casbin()
    res = e.add_policy(authority_info.authority_id, authority_info.path, authority_info.method)
    if res:
        return response_code.resp_200()
    else:
        return response_code.resp_4001(message="添加失败，权限已存在")


@router.post("/del/auth", summary="删除访问权限")
async def del_authority(
        authority_info: AuthCreate
):
    e = get_casbin()
    res = e.remove_policy(authority_info.authority_id, authority_info.path, authority_info.method)
    if res:
        return response_code.resp_200()
    else:
        return response_code.resp_4001(message="删除失败，权限不存在")
