from .user import user_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(user_router, prefix='/users', tags=['users'])
__all__ = ['router']