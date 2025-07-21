from clients.authentication.authentication_client import LoginRequestDict
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.faker import get_random_email
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict

# Инициализируем паблик клиента
public_users_client = get_public_users_client()

# Подготавливаем данные для создания юзера
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

# Создаем юзера
create_user_response = public_users_client.create_user(create_user_request)
print(create_user_response)

# Подготавливаем данные для аутентификации юзера
authentication_user = LoginRequestDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# Инициализируем файл, курс, эксерсайс клиентов
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Подготавливаем данные для создания файла
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image (1).png"
)

#Создаем файл
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ', create_file_response)

# Подготавливаем данные для создания курса
create_course_request = CreateCourseRequestDict(
    title="string",
    maxScore=100,
    minScore=0,
    description="string",
    estimatedTime="1w",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

# Создаем курс
create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ', create_course_response)

# Подготавливаем данные для создания задания
create_exercise_request = CreateExerciseRequestDict(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=30,
    minScore=5,
    orderIndex=1,
    description="Need to done exercise",
    estimatedTime="5h"
)

# Создаем задание
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data: ', create_exercise_response)