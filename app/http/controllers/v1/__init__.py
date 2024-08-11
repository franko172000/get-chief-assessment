from fastapi import APIRouter, Depends
from .auth import router as auth_router
from .user import router as user_router
from .task import router as task_router
from ...middlewares.jwt_auth_middleware import JWTAuthMiddleware

router = APIRouter(prefix="/v1")
router.include_router(auth_router)

protected_router = APIRouter(dependencies=[Depends(JWTAuthMiddleware())])
protected_router.include_router(task_router)
protected_router.include_router(user_router)

router.include_router(protected_router)

__all__ = ["router"]