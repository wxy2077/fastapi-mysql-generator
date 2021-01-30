#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 20:33
# @Author  : CoderCharm
# @File    : sys_schedule.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
初始化 apscheduler
模仿 redis

"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


class ScheduleCli(object):

    def __init__(self):
        # 对象 在 @app.on_event("startup") 中初始化
        self._schedule = None

    def init_scheduler(self) -> None:
        """
        初始化 apscheduler
        :return:
        """
        job_stores = {
            'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        }
        self._schedule = AsyncIOScheduler(jobstores=job_stores)
        self._schedule.start()

    # 使实例化后的对象 赋予apscheduler对象的方法和属性
    def __getattr__(self, name):
        return getattr(self._schedule, name)

    def __getitem__(self, name):
        return self._schedule[name]

    def __setitem__(self, name, value):
        self._schedule[name] = value

    def __delitem__(self, name):
        del self._schedule[name]


# 创建schedule对象 但是这种方式使用方法时没有提示
schedule = ScheduleCli()

# 只允许导出 redis_client 实例化对象
__all__ = ["schedule"]
