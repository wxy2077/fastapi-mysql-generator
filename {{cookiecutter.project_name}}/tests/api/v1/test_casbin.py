#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 10:00
# @Author  : CoderCharm
# @File    : test_casbin.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
测试casbin权限是否有效
"""

from fastapi.testclient import TestClient


def test_ordinary_add_auth(client: TestClient, ordinary_token_headers: dict):
    """
    测试普通用户设置权限是否被拦截
    :return:
    """
    response = client.post("/add/auth", json={
        "authority_id": "100",
        "path": "/add/auth",
        "method": "POST"
    }, headers=ordinary_token_headers)

    assert response.status_code == 200
    assert response.json()["code"] == 4003


def test_ordinary_del_auth(client: TestClient, ordinary_token_headers: dict):
    """
    测试普通用户删除权限是否被拦截
    :return:
    """
    response = client.post("/del/auth", json={
        "authority_id": "100",
        "path": "/add/auth",
        "method": "POST"
    }, headers=ordinary_token_headers)

    assert response.status_code == 200
    assert response.json()["code"] == 4003


def test_admin_add_auth(client: TestClient, superuser_token_headers: dict):
    """
    测试管理员设置权限是否被拦截
    :return:
    """
    response = client.post("/add/auth", json={
        "authority_id": "100",
        "path": "/add/auth",
        "method": "POST"
    }, headers=superuser_token_headers)
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_admin_del_auth(client: TestClient, superuser_token_headers: dict):
    """
    测试管理员删除权限是否被拦截
    :return:
    """
    response = client.post("/del/auth", json={
        "authority_id": "100",
        "path": "/add/auth",
        "method": "POST"
    }, headers=superuser_token_headers)

    assert response.status_code == 200
    assert response.json()["code"] == 200
