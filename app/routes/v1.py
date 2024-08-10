from fastapi import APIRouter
from app.http.controllers.v1 import auth_controller

router = APIRouter(prefix="/api/v1")
router.include_router(auth_controller.auth_router)