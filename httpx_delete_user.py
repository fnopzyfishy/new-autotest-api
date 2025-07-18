import httpx
from tools.faker import get_random_email

payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response = httpx.post(url="http://localhost:8000/api/v1/users", json=payload)
response_json = response.json()
print(response.status_code)
print(response_json)

# Пройти аутентификацию
login_payload = {
  "email": response_json['user']['email'],
  "password": 'string'
}

response_login = httpx.post(url='http://localhost:8000/api/v1/authentication/login', json=login_payload)
response_login_json = response_login.json()
print(response_login.status_code)
print(response_login_json)

# Удалить юзера
access_token_response = response_login_json['token']['accessToken']
headers_auth = {
    "Authorization": f"Bearer {access_token_response}"
}
response_delete = httpx.delete(
    url=f'http://localhost:8000/api/v1/users/{response_json["user"]["id"]}',
    headers=headers_auth
)
print(response_delete.status_code)
print(response_delete.json()) #Возвращает пустой ответ -> None
