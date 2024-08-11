from app.http.controllers.v1.user.dto.user_request import CreateUserRequest
from app.persistence.models import User
from app.persistence.reposiroties.user_repository import UserRepository
from app.services.base_service import BaseService


class UserService(BaseService):

    async def create_user(self, data: CreateUserRequest) -> User:
        return await UserRepository(self.db).create_user(User(
            last_name=data.last_name,
            first_name=data.first_name,
            email=data.email,
            password=data.password
        ))

    async def get_users(self):
        return await UserRepository(self.db).list_users()
