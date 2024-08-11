from datetime import datetime
from typing import List

from pydantic import BaseModel

# from app.http.controllers.v1.task.dto.task_response import TaskResponse


class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        orm_mode = True
