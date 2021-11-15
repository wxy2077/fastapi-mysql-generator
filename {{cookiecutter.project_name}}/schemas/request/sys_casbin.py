"""
校验casbin
"""

from pydantic import BaseModel


# 创建API
class AuthCreate(BaseModel):
    authority_id: str
    path: str
    method: str
