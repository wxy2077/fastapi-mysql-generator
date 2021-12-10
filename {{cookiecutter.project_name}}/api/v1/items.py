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

from tempfile import NamedTemporaryFile
from pathlib import Path

from fastapi import APIRouter, File, UploadFile, Query

from schemas.response import resp
from core.config import settings
from common.sys_redis import redis_client
from models.users import User

router = APIRouter()


@router.get("/test", name="测试接口")
def items_test(
        *,
        bar: str = Query(..., title="测试字段", description="测试字段描述")
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

    return resp.ok(data=redis_test)


@router.get("/user/all", summary="获取所有用户信息", name="获取用户信息")
def get_all_user_info(
        page: int = Query(1),  # 分页等通用字段可以提取出来封装
        page_size: int = Query(20),
):
    user, pagination = User().fetch_all(page=page,page_size=page_size)

    return resp.ok(data=user, pagination=pagination)


@router.post("/upload/file", summary="上传图片", name="上传图片")
def upload_image(
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

    return resp.ok(data={"image": f"/static/img/{tmp_file_name}"})
