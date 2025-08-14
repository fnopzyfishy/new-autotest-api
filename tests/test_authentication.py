from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema

@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client = get_public_users_client()
    authentication_user = get_authentication_client()

    user_request = CreateUserRequestSchema()
    user_response = public_users_client.create_user(user_request)

    login_request = LoginRequestSchema(
        email=user_request.email,
        password=user_request.password
    )

    login_response = authentication_user.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())