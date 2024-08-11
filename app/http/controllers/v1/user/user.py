from typing import List

from fastapi import APIRouter, Depends

from app.core.db.database import get_db
from app.http.controllers.v1.user.dto.user_response import UserResponse
from app.services.user_service import UserService
from app.http.controllers.v1.user.dto.user_request import CreateUserRequest

user_router = APIRouter()


@user_router.post('/')
async def create_user(request: CreateUserRequest, db: get_db = Depends()):
    _user_service = UserService(db)
    return await _user_service.create_user(request)


@user_router.get('/', response_model=List[UserResponse])
async def list_users(db: get_db = Depends()):
    _user_service = UserService(db)
    return await _user_service.get_users()

