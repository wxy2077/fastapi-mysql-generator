#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 16:58
# @Author  : CoderCharm
# @File    : logger.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

日志文件配置 参考链接
https://github.com/Delgan/loguru

# 本来是想 像flask那样把日志对象挂载到app对象上，作者建议直接使用全局对象
https://github.com/tiangolo/fastapi/issues/81#issuecomment-473677039

考虑是否应该把logger 改成单例

"""

import os
import time
from loguru import logger

from core.config import settings

# 定位到log日志文件
log_path = os.path.join(settings.BASE_PATH, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_info = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_info.log')
log_path_warning = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_warning.log')
log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

# 日志简单配置 文件区分不同级别的日志
logger.add(log_path_info, rotation="500 MB", encoding='utf-8', enqueue=True, level='INFO')
logger.add(log_path_warning, rotation="500 MB", encoding='utf-8', enqueue=True, level='WARNING')
logger.add(log_path_error, rotation="500 MB", encoding='utf-8', enqueue=True, level='ERROR')


__all__ = ["logger"]
