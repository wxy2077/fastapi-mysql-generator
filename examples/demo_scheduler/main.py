#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 20:08
# @Author  : CoderCharm
# @File    : main.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

基础的任务调度演示

"""
import time
from typing import Union
from datetime import datetime

from fastapi import FastAPI, Query, Body
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.cron import CronTrigger

Schedule = AsyncIOScheduler(
    jobstores={
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    }
)
Schedule.start()

app = FastAPI()


# 简单定义返回
def resp_ok(*, code=0, msg="ok", data: Union[list, dict, str] = None) -> dict:
    return {"code": code, "msg": msg, "data": data}


def resp_fail(*, code=1, msg="fail", data: Union[list, dict, str] = None):
    return {"code": code, "msg": msg, "data": data}


def cron_task(a1: str) -> None:
    print(a1, time.strftime("'%Y-%m-%d %H:%M:%S'"))


@app.get("/jobs/all", tags=["schedule"], summary="获取所有job信息")
async def get_scheduled_syncs():
    """
    获取所有job
    :return:
    """
    schedules = []
    for job in Schedule.get_jobs():
        schedules.append(
            {"job_id": job.id, "func_name": job.func_ref, "func_args": job.args, "cron_model": str(job.trigger),
             "next_run": str(job.next_run_time)}
        )
    return resp_ok(data=schedules)


@app.get("/jobs/once", tags=["schedule"], summary="获取指定的job信息")
async def get_target_sync(
        job_id: str = Query("job1", title="任务id")
):
    job = Schedule.get_job(job_id=job_id)

    if not job:
        return resp_fail(msg=f"not found job {job_id}")

    return resp_ok(
        data={"job_id": job.id, "func_name": job.func_ref, "func_args": job.args, "cron_model": str(job.trigger),
              "next_run": str(job.next_run_time)})


# interval 固定间隔时间调度
@app.post("/job/interval/schedule/", tags=["schedule"], summary="开启定时:间隔时间循环")
async def add_interval_job(
        seconds: int = Body(120, title="循环间隔时间/秒,默认120s", embed=True),
        job_id: str = Body(..., title="任务id", embed=True),
        run_time: int =Body(time.time(), title="第一次运行时间", description="默认立即执行", embed=True)
):
    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{job_id} job already exists")
    schedule_job = Schedule.add_job(cron_task,
                                    'interval',
                                    args=(job_id,),
                                    seconds=seconds,  # 循环间隔时间 秒
                                    id=job_id,  # job ID
                                    next_run_time=datetime.fromtimestamp(run_time)  # 立即执行
                                    )
    return resp_ok(data={"job_id": schedule_job.id})


# date 某个特定时间点只运行一次
@app.post("/job/date/schedule/", tags=["schedule"], summary="开启定时:固定只运行一次时间")
async def add_date_job(
        run_time: int = Body(..., title="时间戳", description="固定只运行一次时间", embed=True),
        job_id: str = Body(..., title="任务id", embed=True),
):
    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{job_id} job already exists")
    schedule_job = Schedule.add_job(cron_task,
                                    'date',
                                    args=(job_id,),
                                    run_date=datetime.fromtimestamp(run_time),
                                    id=job_id,  # job ID
                                    )
    return resp_ok(data={"job_id": schedule_job.id})


# cron 更灵活的定时任务 可以使用crontab表达式
@app.post("/job/cron/schedule/", tags=["schedule"], summary="开启定时:crontab表达式")
async def add_cron_job(
        job_id: str = Body(..., title="任务id", embed=True),
        crontab: str = Body('*/1 * * * *', title="crontab 表达式"),
        run_time: int =Body(time.time(), title="第一次运行时间", description="默认立即执行", embed=True)
):
    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{job_id} job already exists")
    schedule_job = Schedule.add_job(cron_task,
                                    CronTrigger.from_crontab(crontab),
                                    args=(job_id,),
                                    id=job_id,  # job ID
                                    next_run_time=datetime.fromtimestamp(run_time)
                                    )
    return resp_ok(data={"job_id": schedule_job.id})


@app.post("/job/del", tags=["schedule"], summary="移除任务")
async def remove_schedule(
        job_id: str = Body(..., title="任务id", embed=True)
):
    res = Schedule.get_job(job_id=job_id)
    if not res:
        return resp_fail(msg=f"not found job {job_id}")
    Schedule.remove_job(job_id)
    return resp_ok()

# 暂停和恢复任务 暂时没看


if __name__ == "__main__":
    import uvicorn

    # 官方推荐是用命令后启动 uvicorn main:app --host=127.0.0.1 --port=8150 --reload
    uvicorn.run(app='main:app', host="127.0.0.1", port=8151, reload=False, debug=True)
