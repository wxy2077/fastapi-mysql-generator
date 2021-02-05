#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 20:18
# @Author  : CoderCharm
# @File    : test_user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
需要安装 pytest
pip install pytest

"""

from fastapi.testclient import TestClient


def test_login(client: TestClient) -> None:
    """
    测试登录
    自行使用 /app/create_user.py 创建任意测试用户
    test@test.com
    test
    :return:
    """
    response = client.post("/admin/auth/login/access-token", json={
        "username": "test@test.com",
        "password": "test"
    })
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["data"]["token"]


def test_get_user(client: TestClient):
    """
    测试获取用户信息的接口
    :return:
    """
    response = client.post("/admin/auth/login/access-token", json={
        "username": "test@test.com",
        "password": "test"
    })
    token = response.json()["data"]["token"]

    response = client.get("/admin/auth/user/info", headers={
        "token": token
    })

    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert isinstance(response.json()["data"]["nickname"], str)
