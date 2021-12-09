#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 13:32
# @Author  : CoderCharm
# @File    : response_code.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

统一响应状态码

"""
from typing import Union

from fastapi import status as http_status
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder


class Resp(object):
    def __init__(self, status: int, msg: str, code: int):
        self.status = status
        self.msg = msg
        self.code = code


InvalidRequest: Resp = Resp(1000, "无效的请求", http_status.HTTP_400_BAD_REQUEST)
InvalidParams: Resp = Resp(1002, "无效的参数", http_status.HTTP_400_BAD_REQUEST)
BusinessError = {"status": 1003, "msg": "业务错误", "code": http_status.HTTP_400_BAD_REQUEST}
DataNotFound = {"status": 1004, "msg": "查询失败", "code": http_status.HTTP_400_BAD_REQUEST}
DataStoreFail = {"status": 1005, "msg": "新增失败", "code": http_status.HTTP_400_BAD_REQUEST}
DataUpdateFail = {"status": 1006, "msg": "更新失败", "code": http_status.HTTP_400_BAD_REQUEST}
DataDestroyFail = {"status": 1007, "msg": "删除失败", "code": http_status.HTTP_400_BAD_REQUEST}
PermissionDenied = {"status": 1008, "msg": "权限拒绝", "code": http_status.HTTP_403_FORBIDDEN}


def ok(*, data: Union[list, dict, str] = None, pagination: dict = None, msg: str = "Success") -> Response:
    return JSONResponse(
        status_code=http_status.HTTP_200_OK,
        content=jsonable_encoder({
            'status': 200,
            'msg': msg,
            'data': data,
            'pagination': pagination
        })
    )


def fail(resp: Resp) -> Response:
    return JSONResponse(
        status_code=resp.code,
        content=jsonable_encoder({
            'status': resp.status,
            'msg': resp.msg,
        })
    )
