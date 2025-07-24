from clients.authentication.authentication_client import LoginRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.faker import get_random_email
from clients.exercises.exercises_client import get_exercises_client

# Инициализируем паблик клиента
public_users_client = get_public_users_client()

# Подготавливаем данные для создания юзера
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

# Создаем юзера
create_user_response = public_users_client.create_user(create_user_request)
print(create_user_response)

# Подготавливаем данные для аутентификации юзера
authentication_user = LoginRequestSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Инициализируем файл, курс, эксерсайс клиентов
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Подготавливаем данные для создания файла
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image (1).png"
)

#Создаем файл
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ', create_file_response)

# Подготавливаем данные для создания курса
create_course_request = CreateCourseRequestSchema(
    title="string",
    max_score=100,
    min_score=0,
    description="string",
    estimated_time="1w",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

# Создаем курс
create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ', create_course_response)

# Подготавливаем данные для создания задания
create_exercise_request = CreateExerciseRequestSchema(
    title="Exercise 1",
    course_id=create_course_response.course.id,
    max_score=30,
    min_score=5,
    order_index=1,
    description="Need to done exercise",
    estimated_time="5h"
)

# Создаем задание
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data: ', create_exercise_response)