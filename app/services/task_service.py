from typing import Type

from fastapi import HTTPException
from starlette import status

from app.http.controllers.v1.task.dto.task_request import TaskRequest
from app.persistence.models import Task
from app.persistence.reposiroties.task_repository import TaskRepository
from app.persistence.reposiroties.user_repository import UserRepository
from app.services.base_service import BaseService


class TaskService(BaseService):

    def create_task(self, task: TaskRequest) -> dict[str, str] | Task:
        new_task = Task(
            title=task.title,
            description=task.description,
            status=task.status,
            priority=task.priority,
            due_date=task.due_date,
            assigned_date=task.assigned_date,
        )

        if task.owner_id:
            new_task.owner_id = task.owner_id
            # check if user exists
            UserRepository(self.db).find_or_fail_by_id(task.owner_id)

        return TaskRepository(self.db).create_task(new_task)

    def get_user_tasks(self, user_id: int) -> list[Type[Task]]:
        return TaskRepository(self.db).list_user_tasks(user_id)

    def get_tasks(self) -> list[Type[Task]]:
        return TaskRepository(self.db).list_tasks()

    def unassign(self, task_id: int) -> Task:
        return TaskRepository(self.db).unassign_tasks(task_id)

    def assign(self, task_id: int, owner_id: int) -> Task:
        UserRepository(self.db).find_or_fail_by_id(owner_id)
        return TaskRepository(self.db).assign_tasks(task_id, owner_id)

    def update_task(self, user_id: int, task: TaskRequest) -> Task:
        return TaskRepository(self.db).update_task(user_id, task)

    def get_task(self, task_id: int) -> Task:
        return TaskRepository(self.db).find_or_fail_by_id(task_id)

    def delete_task(self, task_id: int) -> None:
        return TaskRepository(self.db).delete_task(task_id)
