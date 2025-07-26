from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema

# Инициализируем клиента PublicUsersClient
public_users_client = get_public_users_client()

# Подготавливаем данные для работы с PublicUsersClient
create_user_request = CreateUserRequestSchema()

# Делаем запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Подготавливаем данные аутентификации(берем данные с запроса на создание)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
# Инициализируем приват клиента
private_users_client = get_private_users_client(authentication_user)

# Берем данные юзера
get_user_response = private_users_client.get_user_api(create_user_response.user.id)
print('Get user data:', get_user_response)