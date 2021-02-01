#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 13:50
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

配置文件区分生产和开发

我这种是一种方式，简单直观
还有一种是服务一个固定路径放一个配置文件如 /etc/conf 下 xxx.ini 或者 xxx.py文件
然后项目默认读取 /etc/conf 目录下的配置文件，能读取则为生产环境，
读取不到则为开发环境，开发环境配置可以直接写在代码里面(或者配置ide环境变量)

根据环境变量ENV是否有值 区分生产开发

"""

import os

# 获取环境变量
env = os.getenv("ENV", "")
if env:
    # 如果有虚拟环境 则是 生产环境
    print("----------生产环境启动------------")
    from .production_config import settings
else:
    # 没有则是开发环境
    print("----------开发环境启动------------")
    from .development_config import settings
