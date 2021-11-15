"""

"""
from typing import Dict
from fastapi.testclient import TestClient


def user_authentication_headers(
        *, client: TestClient, email: str, password: str
) -> Dict[str, str]:
    data = {"username": email,
            "password": password}

    resp = client.post("/admin/auth/login/access-token", json=data)
    response = resp.json()
    token = response["data"]["token"]
    headers = {"token": token}
    return headers
