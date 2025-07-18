from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class UpdateUserRequestDict(TypedDict):
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.client.get(url='/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        return self.client.get(url=f'/api/v1/users/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        return self.client.patch(url=f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        return self.client.delete(url=f'/api/v1/users/{user_id}')