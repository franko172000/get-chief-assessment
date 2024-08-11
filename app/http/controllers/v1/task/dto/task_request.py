from typing import Optional

from pydantic import BaseModel


class TaskRequest(BaseModel):
    title: str
    description: str
    status: str
    owner_id: Optional[int]


class AssignTaskRequest(BaseModel):
    user_id: int
