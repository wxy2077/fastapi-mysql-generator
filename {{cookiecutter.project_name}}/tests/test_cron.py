#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 11:49
# @Author  : CoderCharm
# @File    : test_cron.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
测试任务调度

暂时有问题

"""

import os
import sys

# 解决包导入问题
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# from fastapi.testclient import TestClient
# from core.server import create_app
#
# app = create_app()
#
# client = TestClient(app)
#
#
# def test_add_job():
#     response = client.post("/job/schedule", json={
#         "seconds": 5,
#         "job_id": "666"
#     })
#     assert response.status_code == 200
#     assert response.json()["code"] == 200
#     assert response.json()["data"]["id"] == "666"


# def test_get_all_job():
#     response = client.get("/jobs/all")
#     assert response.status_code == 200
#     assert response.json()["code"] == 200
#     assert isinstance(response.json()["data"], list)
#
#
# def test_del_job():
#     response = client.post("/job/del", json={
#         "job_id": JOB_ID
#     })
#     assert response.status_code == 200
#     assert response.json()["code"] == 200
#     assert isinstance(response.json()["data"], list)
