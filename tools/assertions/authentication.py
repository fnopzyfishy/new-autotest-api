from tools.assertions.base import assert_equal, assert_is_true
from clients.authentication.authentication_schema import LoginResponseSchema

def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response:
    :return:
    """
    assert_equal(response.token.token_type, "bearer", "token_type")
    assert_is_true(response.token.access_token, "accessToken")
    assert_is_true(response.token.refresh_token, "refreshToken")