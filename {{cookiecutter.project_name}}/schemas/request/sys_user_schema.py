#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:43
# @Author  : CoderCharm
# @File    : sys_user_schema.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
管理员表的 字段model模型 验证 响应(没写)等
"""

from typing import Optional

from pydantic import BaseModel, EmailStr, AnyHttpUrl


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    phone: int = None
    is_active: Optional[bool] = True


class UserAuth(BaseModel):
    password: str


# 邮箱登录认证 验证数据字段都叫username
class UserEmailAuth(UserAuth):
    username: EmailStr


# 手机号登录认证 验证数据字段都叫username
class UserPhoneAuth(UserAuth):
    username: int


# 创建账号需要验证的条件
class UserCreate(UserBase):
    nickname: str
    email: EmailStr
    password: str
    authority_id: int = 1
    avatar: Optional[AnyHttpUrl] = None


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str


# 返回的用户信息
class UserInfo(BaseModel):
    role_id: int
    role: str
    nickname: str
    avatar: AnyHttpUrl

