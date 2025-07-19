from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from httpx import Response
from typing import TypedDict

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class UpdateUserRequestDict(TypedDict):
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class GetUserResponseDict(TypedDict):
    user: User

class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.client.get(url='/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        return self.client.get(url=f'/api/v1/users/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        return self.client.patch(url=f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        return self.client.delete(url=f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()

def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))