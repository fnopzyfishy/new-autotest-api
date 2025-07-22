import uuid
from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError


class UserSchema(BaseModel):
    """
    Реализация юзер схемы
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName", default="string")
    first_name: str = Field(alias="firstName", default="string")
    middle_name: str = Field(alias="middleName", default="string")


class CreateUserRequestSchema(BaseModel):
    """
    Реализация схемы создания юзера(запрос)
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName", default="string")
    first_name: str = Field(alias="firstName", default="string")
    middle_name: str = Field(alias="middleName", default="string")


class CreateUserResponseSchema(BaseModel):
    """
    Реализация схемы создания юзера(ответ)
    """
    user: UserSchema
