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
from fastapi import APIRouter, Depends, Request, File, UploadFile, Query

from api.v1.auth.crud.user import curd_user
from common import deps, response_code
from core.config import settings

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

    # 用不惯orm查询的可以直接sql(建议把CURD操作单独放到其他文件夹下,统一管理)
    test_sql = "SELECT * from admin_user WHERE id>=:id"
    admin_user_res = db.execute(text(test_sql), {"id": 1}).fetchall()

    return response_code.resp_200(data={
        "items": "ok",
        "admin_user_info": admin_user_res,
        "redis_test": redis_test
    })


@router.get("/user/all", summary="获取所有用户信息")
async def get_all_user_info(
        page: int = Query(1),  # 分页等通用字段可以提取出来封装
        page_size: int = Query(20),
        db: Session = Depends(deps.get_db),
):
    all_user = curd_user.get_multi(db=db, page=page, page_size=page_size)
    return response_code.resp_200(data=all_user)


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
