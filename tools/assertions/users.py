from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal

def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request:
    :param response:
    :return:
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(request: UserSchema, response: UserSchema):
    """
    Проверяет, что данные юзера в ответе, такие же как в запросе.

    :param request:
    :param response:
    :return:
    """
    assert_equal(response.id, request.id, "id")
    assert_equal(response.email, request.email, "email")
    assert_equal(response.last_name, request.last_name, "last_name")
    assert_equal(response.first_name, request.first_name, "first_name")
    assert_equal(response.middle_name, request.middle_name, "middle_name")

def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Проверяет только юзера из ответов.

    :param get_user_response:
    :param create_user_response:
    :return:
    """
    assert_user(get_user_response.user, create_user_response.user)