"""
开发环境配置
"""
import os

from typing import Union, Optional

from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Settings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = True
    # 项目文档
    TITLE: str = "FastAPI+MySQL项目生成"
    DESCRIPTION: str = "FastAPI"
    # 文档地址 默认为docs
    DOCS_URL: str = "/api/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/api/redoc"

    # token过期时间 分钟
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # 生成token的加密算法
    ALGORITHM: str = "HS256"

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = 'aeq)s(*&(&)()WEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = "root"
    MYSQL_PASSWORD: str = "Admin12345-"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = 'temp_db_date'

    # Mysql地址
    SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis配置
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PASSWORD: str = "root12345"
    REDIS_DB: int = 0
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"
    REDIS_TIMEOUT: int = 5  # redis连接超时时间

    CASBIN_MODEL_PATH: str = "./resource/rbac_model.conf"


settings = Settings()
