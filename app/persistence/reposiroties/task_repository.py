from typing import Type

from sqlalchemy.orm import Session

from app.http.controllers.v1.task.dto.task_request import TaskRequest
from app.persistence.models import Task
from app.persistence.reposiroties.base_repository import BaseRepository


class TaskRepository(BaseRepository):

    def __init__(self, db: Session):
        self._model = Task
        super().__init__(db)

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

    def assign_tasks(self, task_id: int, owner_id: int) -> Task:
        task = self.find_or_fail_by_id(task_id)
        task.owner_id = owner_id
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: int, task_data: TaskRequest) -> Task:
        task = self.find_or_fail_by_id(task_id)
        for key, value in task_data.model_dump().items():
            setattr(task, key, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int) -> None:
        task = self.find_or_fail_by_id(task_id)
        self.db.delete(task)
        self.db.commit()
