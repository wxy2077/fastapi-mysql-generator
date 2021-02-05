#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 14:00
# @Author  : CoderCharm
# @File    : user.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""
from typing import Dict
from fastapi.testclient import TestClient


def user_authentication_headers(
        *, client: TestClient, email: str, password: str
) -> Dict[str, str]:
    data = {"username": email,
            "password": password}

    resp = client.post("/admin/auth/login/access-token", json=data)
    response = resp.json()
    token = response["data"]["token"]
    headers = {"token": token}
    return headers
