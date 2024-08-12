from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

# from app.http.controllers.v1.task.dto.task_response import TaskResponse


class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    created_at: datetime
    task_count: Optional[int] = None

    class Config:
        orm_mode = True
