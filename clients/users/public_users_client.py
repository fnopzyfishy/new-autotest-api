from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateUserDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя
        :return:
        """

        return self.client.post('/api/v1/users', json=request)