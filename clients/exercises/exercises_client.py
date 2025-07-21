from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minscore: int
    orderIndex: int
    description: str
    estimatedTime: str

class Exercises(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class GetExercisesQueryDict(TypedDict):
    courseId: str

class GetExerciseResponseDict(TypedDict):
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    exercises: Exercises

class ExercisesClient(APIClient):
    """
    Методы работы с блоком Exercises в API
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        return self.client.get(url='/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.client.get(url=f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        return self.client.post(url='/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        return self.client.patch(url=f'/api/v1/exercise/{exercise_id}', json=request)

    def delete_execise_api(self, exercise_id: str) -> Response:
        return self.client.delete(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> GetExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> GetExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция для инициализации exercise клиента
    :param user:
    :return:
    """
    return ExercisesClient(client=get_private_http_client(user))