from .task import task_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(task_router, prefix='/tasks', tags=['tasks'])
__all__ = ['router']