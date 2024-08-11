from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
