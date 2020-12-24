#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 15:03
# @Author  : CoderCharm
# @File    : celery_app.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""


from celery import Celery

celery_app = Celery("worker", broker="amqp://guest@queue//")

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
