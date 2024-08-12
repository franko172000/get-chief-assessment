from typing import List

from fastapi import APIRouter, Depends

from app.core.db.database import get_db
from app.http.controllers.v1.user.dto.user_response import UserResponse
from app.services.user_service import UserService
from app.http.controllers.v1.user.dto.user_request import CreateUserRequest

user_router = APIRouter()


@user_router.post('/', response_model=UserResponse)
async def create_user(request: CreateUserRequest, db: get_db = Depends()):
    return UserService(db).create_user(request)


@user_router.get('/', response_model=List[UserResponse])
async def list_users(db: get_db = Depends()):
    _user_service = UserService(db)
    return _user_service.get_users()


@user_router.delete('/{user_id}')
async def delete_user(user_id: int, db: get_db = Depends()):
    UserService(db).delete_users(user_id)
    return
