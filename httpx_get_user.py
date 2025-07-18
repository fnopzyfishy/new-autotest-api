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
print(response_login.status_code)
print(response_login.json())