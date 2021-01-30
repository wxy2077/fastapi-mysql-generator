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
from fastapi import APIRouter, Depends, File, UploadFile, Query

from service.sys_user import curd_user
from common import deps
from schemas.response import response_code
from core.config import settings
from db.sys_redis import redis_client

router = APIRouter()


@router.get("/test", summary="用户登录认证", name="测试接口")
async def items_test(
        *,
        bar: str = Query(..., title="测试字段", description="测试字段描述"),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    用户登录
    :param bar:
    :param db:
    :return:
    """
    # 测试redis使用
    redis_client.set("test_items", bar, ex=60)
    redis_test = redis_client.get("test_items")

    # 用不惯orm查询的可以直接sql(建议把CURD操作单独放到service文件夹下,统一管理)
    test_sql = "SELECT nickname,avatar from sys_user WHERE id>=:id"
    admin_user_res = db.execute(text(test_sql), {"id": 1}).fetchall()

    return response_code.resp_200(data={
        "items": "ok",
        "admin_user_info": admin_user_res,
        "redis_test": redis_test
    })


@router.get("/user/all", summary="获取所有用户信息", name="获取用户信息")
async def get_all_user_info(
        page: int = Query(1),  # 分页等通用字段可以提取出来封装
        page_size: int = Query(20),
        db: Session = Depends(deps.get_db),
):
    all_user = curd_user.get_multi(db=db, page=page, page_size=page_size)
    return response_code.resp_200(data=all_user)


@router.post("/upload/file", summary="上传图片", name="上传图片")
async def upload_image(
        file: UploadFile = File(...),
):
    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    # 建议计算并记录一次 文件md5值 避免重复存储相同资源
    save_dir = f"{settings.BASE_PATH}/static/img"

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
