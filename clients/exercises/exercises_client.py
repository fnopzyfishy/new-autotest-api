from clients.api_client import APIClient
from httpx import Response
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client

class ExercisesClient(APIClient):
    """
    Методы работы с блоком Exercises в API
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        return self.client.get(url='/api/v1/exercises', params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.client.get(url=f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        return self.client.post(url='/api/v1/exercises', json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        return self.client.patch(url=f'/api/v1/exercise/{exercise_id}', json=request.model_dump(by_alias=True))

    def delete_execise_api(self, exercise_id: str) -> Response:
        return self.client.delete(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> GetExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> GetExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция для инициализации exercise клиента
    :param user:
    :return:
    """
    return ExercisesClient(client=get_private_http_client(user))