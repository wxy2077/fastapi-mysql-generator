#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 13:23
# @Author  : CoderCharm
# @File    : production_config.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
生产环境配置

我这种是一种方式，简单直观
服务器上设置 ENV 环境变量

还有一种是服务一个固定路径放一个配置文件如 /etc/conf 下 xxx.ini 或者 xxx.py文件
然后项目默认读取 /etc/conf 目录下的配置文件，能读取则为生产环境，
读取不到则为开发环境，开发环境配置可以直接写在代码里面(或者配置ide环境变量)


"""

import os

from typing import Union, Optional

from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Settings(BaseSettings):
    # 生产模式配置
    DEBUG: bool = False
    # 项目文档
    TITLE: str = "FastAPI+MySql项目生成"
    DESCRIPTION: str = "更多FastAPI知识，请关注我的个人网站 https://www.charmcode.cn/"

    # 文档地址 生产环境关闭 None
    DOCS_URL: Optional[str] = None
    # 文档关联请求数据接口 生产环境关闭 None
    OPENAPI_URL: Optional[str] = None
    # 生产环境关闭 redoc 文档
    REDOC_URL: Optional[str] = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM = "HS256"

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    # 生产环境项目根路径
    BASE_PATH: str = "/data"

    # MySql配置
    MYSQL_USERNAME: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "admin")
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_DATABASE: str = os.getenv("MYSQL_DB", "xxx")

    # MySql地址
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis配置
    REDIS_HOST: str = os.getenv("REDIS_HOST", "root")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "12345")
    REDIS_DB: int = 0
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"

    CASBIN_MODEL_PATH: str = "./resource/rbac_model.conf"


settings = Settings()

