from fastapi import HTTPException
from starlette import status
from app.persistence.reposiroties.user_repository import UserRepository
from app.persistence.models import User
from app.services.base_service import BaseService
from app.http.controllers.v1.user.dto.user_request import CreateUserRequestDto


class UserService(BaseService):

    def create_user(self, data: CreateUserRequestDto) -> User:
        user_repo = UserRepository(self.db)
        user = user_repo.get_user_by_email(email=data.email)
        if user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already registered')
        return user_repo.create_user(data)

    def get_users(self):
        return UserRepository(self.db).list_users()

    def delete_users(self, user_id):
        return UserRepository(self.db).delete_user(user_id)
