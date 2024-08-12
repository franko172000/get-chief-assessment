from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEnum(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    done = "done"
    testing = "testing"
    blocked = "blocked"


class PriorityEnum(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class TaskRequest(BaseModel):
    title: str
    description: str
    status: Optional[StatusEnum] = StatusEnum.not_started
    owner_id: Optional[int] = None
    description: str
    assigned_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    priority: Optional[PriorityEnum] = None


class AssignTaskRequest(BaseModel):
    owner_id: int
