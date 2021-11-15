"""

"""

from typing import Any
from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from core import security
from common import deps, logger
from core.config import settings
from schemas.response import response_code
from service.sys_user import curd_user

router = APIRouter()

from fastapi.security import OAuth2PasswordRequestForm

@router.post("/access-token", summary="用户登录认证", name="登录")
async def login_access_token(
        *,
        db: Session = Depends(deps.get_db),
        user_info: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    用户JWT登录
    :param db:
    :param user_info:
    :return:
    """

    # 验证用户
    user = curd_user.authenticate(db, email=user_info.username, password=user_info.password)
    if not user:
        logger.info(f"用户邮箱认证错误: email{user_info.username} password:{user_info.password}")
        return response_code.resp_500(message="username or password error")
    elif not curd_user.is_active(user):
        return response_code.resp_500(message="User email not activated")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # 登录token 存储了user.id 和 authority_id
    token = security.create_access_token(user.id, user.authority_id, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
