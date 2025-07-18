from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

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

class ExercisesClient(APIClient):
    """
    Методы работы с блоком Exercises в API
    """
    def get_exercises_api(self, course_id: str) -> Response:
        return self.client.get(url='/api/v1/exercises', params=course_id)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.client.get(url=f'/api/v1/exercises/{exercise_id}')

    def create_exercise(self, request: CreateExerciseRequestDict):
        return self.client.post(url='/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict):
        return self.client.patch(url=f'/api/v1/exercise/{exercise_id}', json=request)

    def delete_execise_api(self, exercise_id: str):
        return self.client.delete(url=f'/api/v1/exercises/{exercise_id}')