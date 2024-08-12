from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from app.core.db.database import get_db
from app.http.controllers.v1.task.dto.task_request import TaskRequest, AssignTaskRequest
from app.http.controllers.v1.task.dto.task_response import TaskResponse
from app.services.task_service import TaskService

task_router = APIRouter()


@task_router.post('', response_model=TaskResponse)
def create_task(data: TaskRequest, db: get_db = Depends()):
    return TaskService(db).create_task(data)


@task_router.get('', response_model=List[TaskResponse])
async def list_tasks(db: get_db = Depends()):
    return TaskService(db).get_tasks()


@task_router.put('/{task_id}', response_model=TaskResponse)
async def update_task(task_id: int, data: TaskRequest, db: get_db = Depends()):
    return TaskService(db).update_task(task_id, data)


@task_router.get('/{task_id}', response_model=TaskResponse)
async def get_task(task_id: int, db: get_db = Depends()):
    return TaskService(db).get_task(task_id)


@task_router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def get_task(task_id: int, db: get_db = Depends()):
    return TaskService(db).delete_task(task_id)


@task_router.get('/user/{user_id}', response_model=List[TaskResponse])
async def list_user_tasks(user_id: int, db: get_db = Depends()):
    return TaskService(db).get_user_tasks(user_id)


@task_router.patch('/{task_id}/unassign', response_model=TaskResponse)
async def unassign_task(task_id: int, db: get_db = Depends()):
    return TaskService(db).unassign(task_id)


@task_router.patch('/{task_id}/assign', response_model=TaskResponse)
async def assign_task(task_id: int, data: AssignTaskRequest, db: get_db = Depends()):
    return TaskService(db).assign(task_id, data.owner_id)
