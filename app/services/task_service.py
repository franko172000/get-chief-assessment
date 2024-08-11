from typing import Dict, List, Type

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
            status=task.status
        )

        if task.owner_id:
            new_task.owner_id = task.owner_id
            # check if user exists
            if not UserRepository(self.db).get_user_by_id(task.owner_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error creating task: User does not "
                                                                                  "exist")

        return TaskRepository(self.db).create_task(new_task)

    def get_user_tasks(self, user_id: int) -> list[Type[Task]]:
        return TaskRepository(self.db).list_user_tasks(user_id)

    def unassign(self, task_id: int) -> Task:
        return TaskRepository(self.db).unassign_tasks(task_id)

    def update_task(self, user_id: int, task: TaskRequest) -> Task:
        return TaskRepository(self.db).update_task(user_id, task)

    def get_task(self, task_id: int) -> Task:
        task = TaskRepository(self.db).get_task_by_id(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
        return task
