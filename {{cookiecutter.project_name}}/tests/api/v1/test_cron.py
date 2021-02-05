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

"""

from fastapi.testclient import TestClient


def test_add_job(
        client: TestClient,
        job_id: str,
        superuser_token_headers: dict
) -> None:
    response = client.post("/job/schedule", json={
        "seconds": 5,
        "job_id": job_id
    }, headers=superuser_token_headers)
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["data"]["id"] == job_id


def test_get_all_job(client: TestClient, superuser_token_headers: dict) -> None:
    response = client.get("/jobs/all", headers=superuser_token_headers)
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert isinstance(response.json()["data"], list)


def test_del_job(client: TestClient, job_id: str, superuser_token_headers: dict) -> None:
    response = client.post("/job/del", json={
        "job_id": job_id
    }, headers=superuser_token_headers)
    assert response.status_code == 200
    assert response.json()["code"] == 200
