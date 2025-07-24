from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from httpx import Response
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema

class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.client.get(url='/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        return self.client.get(url=f'/api/v1/users/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        return self.client.patch(url=f'/api/v1/users/{user_id}', json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        return self.client.delete(url=f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))