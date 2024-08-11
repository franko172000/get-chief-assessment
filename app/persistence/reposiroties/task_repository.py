from typing import List, Type

from fastapi import HTTPException

from app.http.controllers.v1.task.dto.task_request import TaskRequest
from app.persistence.models import User, Task
from app.persistence.reposiroties.base_repository import BaseRepository


class TaskRepository(BaseRepository):
    def create_task(self, task: Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def list_user_tasks(self, user_id: int) -> list[Type[Task]]:
        return self.db.query(Task).filter_by(owner_id=user_id).all()

    def unassign_tasks(self, task_id: int) -> Task:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        task.owner_id = None
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()
        pass

    def update_task(self, task_id: int, task_data: TaskRequest) -> Task:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail='Task not found')

        for key, value in task_data.model_dump().items():
            setattr(task, key, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int) -> None:
        pass
