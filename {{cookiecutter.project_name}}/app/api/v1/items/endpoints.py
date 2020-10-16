#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 15:21
# @Author  : CoderCharm
# @File    : endpoints.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""
import os
from typing import Any
import shutil

from pathlib import Path
from tempfile import NamedTemporaryFile

from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import APIRouter, Depends, Request, File, UploadFile

from app.common import deps, response_code
from app.core.config import settings
from app.utils.tools_func import serialize_sqlalchemy_obj


router = APIRouter()


@router.get("/test", summary="用户登录认证")
async def items_test(
        request: Request,
        *,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    用户登录
    :param request:
    :param db:
    :return:
    """
    await request.app.state.redis.set("test_items", 123, expire=30)
    # 等待 redis读取
    redis_test = await request.app.state.redis.get("test_items")

    # 用不惯orm查询的可以手撸sql 使用 from sqlalchemy import text 可以自动转义字符 避免sql注入
    test_sql = "SELECT * from admin_user WHERE id>=:id"
    admin_user_res = db.execute(text(test_sql), {"id": 1}).fetchall()

    # 手动序列化查询后的结果集
    admin_user_info = serialize_sqlalchemy_obj(admin_user_res)

    return response_code.resp_200(data={
        "items": "ok",
        "admin_user_info": admin_user_info,
        "redis_test": redis_test
    })


@router.post("/upload/file", summary="上传图片")
async def upload_image(
        file: UploadFile = File(...),
):

    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    save_dir = f"{settings.BASE_PATH}/app/static/img"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    try:
        suffix = Path(file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        file.file.close()

    return response_code.resp_200(data={"image": f"/static/img/{tmp_file_name}"})
