from typing import List, Type

from app.persistence.models import User
from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    async def create_user(self, user: User) -> User:
        # user.password = user.password
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    async def list_users(self) -> list[Type[User]]:
        return self.db.query(User).all()

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()
