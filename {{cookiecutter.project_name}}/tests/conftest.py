"""

测试时需要用到的依赖

"""
import os
import sys

# 解决包导入问题
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Generator

import pytest

from fastapi.testclient import TestClient

from core.server import create_app
from db.session import SessionLocal
from tests.utils.user import user_authentication_headers


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """
    FastAPI对象
    :return:
    """
    app = create_app()
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def job_id() -> str:
    """
    测试定时任务用到的 job_id
    :return:
    """
    return "123"


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> dict:
    """
    管理员 admin 用户测试， 后续新增 一份测试环境
    :param client:
    :return:
    """
    return user_authentication_headers(
        client=client,
        email="admin@admin.com",
        password="admin"
    )


@pytest.fixture(scope="module")
def ordinary_token_headers(client: TestClient) -> dict:
    """
    普通用户
    :param client:
    :return:
    """
    return user_authentication_headers(
        client=client,
        email="test@test.com",
        password="test"
    )
