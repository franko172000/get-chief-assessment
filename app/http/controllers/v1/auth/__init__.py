from .auth import auth_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(auth_router, prefix='/auth', tags=['auth'])
__all__ = ['router']