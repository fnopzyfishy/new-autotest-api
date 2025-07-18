import httpx

from tools.faker import get_random_email

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
patch_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

# Создаем юзера
response = httpx.post(url="http://localhost:8000/api/v1/users", json=payload)
response_json = response.json()
print(response.status_code)
print(response_json)

# Подготовка данных
login_payload = {
  "email": response_json['user']['email'],
  "password": 'string'
}
user_id = response_json['user']['id']

# Проходим аутентификацию
response_login = httpx.post(url='http://localhost:8000/api/v1/authentication/login', json=login_payload)
response_login_json = response_login.json()
print(response_login.status_code)
print(response_login_json)
access_token_response = response_login_json['token']['accessToken']
headers_auth_token = {
    "Authorization": f"Bearer {access_token_response}"
}

reponse_patch = httpx.patch(
    url=f'http://localhost:8000/api/v1/users/{user_id}',
    json=patch_payload,
    headers=headers_auth_token
)

print(response.status_code)
print(response.json())