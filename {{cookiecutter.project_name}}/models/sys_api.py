"""

"""

from sqlalchemy import Column, VARCHAR
from db.base_class import Base

class CasbinRule(Base):
    """
    CASBIN表
    """
    ptype = Column(VARCHAR(255), comment="类型:p策略、g角色等等")
    v0 = Column(VARCHAR(255), comment="角色 roleName/roleId   sub")
    v1 = Column(VARCHAR(255), comment="API路径")
    v2 = Column(VARCHAR(255), comment="请求方法")
    v3 = Column(VARCHAR(255), comment="允许读/写 read/write")
    v4 = Column(VARCHAR(255), comment="允许/拒绝 allow/deny")
    v5 = Column(VARCHAR(255), comment="")

    __table_args__ = ({'comment': 'CASBIN管理表'})
    
class SysApi(Base):
    """
    API表
    """
    path = Column(VARCHAR(128), comment="API路径")
    description = Column(VARCHAR(64), comment="API描述")
    api_group = Column(VARCHAR(32), comment="API分组")
    method = Column(VARCHAR(16), comment="请求方法")

    __table_args__ = ({'comment': 'API管理表'})
