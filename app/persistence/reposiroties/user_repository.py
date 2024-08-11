from typing import Type

from sqlalchemy.orm import Session

from app.persistence.models import User
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

    def list_users(self) -> list[Type[User]]:
        return self.db.query(self._model).all()

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(self._model).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(self._model).filter(User.id == user_id).first()
