"""
自定义异常
"""


class TokenAuthError(Exception):
    def __init__(self, err_desc: str = "User Authentication Failed"):
        self.err_desc = err_desc


class TokenExpired(Exception):
    def __init__(self, err_desc: str = "Token has expired"):
        self.err_desc = err_desc


class AuthenticationError(Exception):
    def __init__(self, err_desc: str = "Permission denied"):
        self.err_desc = err_desc

