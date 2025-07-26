from pydantic import Field
from tools.faker import fake
from pydantic import BaseModel

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: str
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="test")
    upload_file: str


# Добавили описание структуры запроса на создание файла
class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema