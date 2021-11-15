"""

"""

from sqlalchemy import Column, VARCHAR
from db.base_class import Base


class SysApi(Base):
    """
    API表
    """
    path = Column(VARCHAR(128), comment="API路径")
    description = Column(VARCHAR(64), comment="API描述")
    api_group = Column(VARCHAR(32), comment="API分组")
    method = Column(VARCHAR(16), comment="请求方法")

    __table_args__ = ({'comment': 'API管理表'})
