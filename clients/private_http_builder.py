from httpx import Client
from typing import TypedDict
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url='http://localhost:8000/',
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
