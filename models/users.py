from pydantic import BaseModel


class UserResponseDto(BaseModel):
    username: str
    email: str
    password: str
    id: str


class UserRequestDto(BaseModel):
    username: str
    email: str
    password: str
