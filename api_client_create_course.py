"""
1. + Инициализировать паблик клиента
2. + Подготовить данные для создание юзера
3. + Создать юзера
4. + Инициализировать данные для аутентификации юзера
5. + Аутентифицировать юзера
6. + Инициализация курс клиента
7. + Подготовить данные для создания курса
8. Создать курс
"""
from clients.authentication.authentication_client import LoginRequestDict
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.faker import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_users_client.create_user(create_user_request)
print(create_user_response)

authentication_user = LoginRequestDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image (1).png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(
    title="string",
    maxScore=1,
    minScore=0,
    description="string",
    estimatedTime="1h",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)
print(create_course_response)