import httpx

main_url = 'http://localhost:8000'
post_authentication = '/api/v1/authentication/login'
get_user_me = '/api/v1/users/me'
body_to_authentication = {
    "email": "usersss1233@example.com",
    "password": "string"
}

"""
1. Получить accessToken из эндпоинта post_authentication 
    1. Код ответа 200
    2. В ответе JSON с токенами
2. Совершить GET-запрос к get_user_me используя токен в заголовке
    1. Код ответа 200
    2. В ответе JSON с данными пользователя
3. Вывести на консоль данные о пользователе и статус-код ответа
"""

def test_get_user_me():
    response = httpx.post(main_url + post_authentication, json=body_to_authentication)
    response_json = response.json()
    print(response.status_code)
    print(response_json) #accessToken -> response_json['token']['accessToken']
    headers = {"Authorization": f"Bearer {response_json['token']['accessToken']}"}

    get_user_meee = httpx.get(main_url + get_user_me, headers=headers)
    print(get_user_meee.status_code)
    print(get_user_meee.json())



test_get_user_me()