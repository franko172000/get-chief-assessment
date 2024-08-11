from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEnum(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    done = "done"
    testing = "testing"
    blocked = "blocked"


class TaskRequest(BaseModel):
    title: str
    description: str
    status: StatusEnum
    owner_id: Optional[int] = None


class AssignTaskRequest(BaseModel):
    owner_id: int
