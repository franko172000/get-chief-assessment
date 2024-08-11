from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.http.controllers.v1.user.dto.user_response import UserResponse


class TaskResponse(BaseModel):
    title: str
    description: str
    status: str
    created_at: datetime
    owner: Optional[UserResponse]

    class Config:
        orm_mode = True
