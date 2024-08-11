from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class CreateUserRequestDto(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
