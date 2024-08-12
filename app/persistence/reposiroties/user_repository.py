from typing import Type

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.persistence.models import User, Task
from .base_repository import BaseRepository
# from ...http.controllers.v1.user.dto.user_request import CreateUserRequestDto

from ...utils.hashing import Hash


class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        self._model = User
        super().__init__(db)

    def create_user(self, data: any) -> User:
        user = User(
            last_name=data.last_name,
            first_name=data.first_name,
            email=data.email,
            password=data.password
        )
        user.password = Hash.hash_password(user.password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def list_users(self):
        test = self.db.query(
            self._model.id, self._model.first_name, self._model.last_name, self._model.email, self._model.created_at, func.count(Task.id).label('task_count')).outerjoin(
            Task).group_by(self._model.id).all()
        return test

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(self._model).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(self._model).filter(User.id == user_id).first()

    def delete_user(self, user_id: int) -> None:
        user = self.find_or_fail_by_id(user_id)
        self.db.delete(user)
        self.db.commit()
        return
