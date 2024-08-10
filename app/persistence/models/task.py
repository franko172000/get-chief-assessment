from sqlalchemy import BaseModel, Integer, Column, String, DateTime, ForeignKey, relationship
from sqlalchemy.orm import Mapped

from .base_model import BaseModel


class Task(BaseModel):
    __tablename__ = 'tasks'
    title = Column(String)
    description = Column(String)
    status = Column(String)
    owner_id: Mapped[int] = Column(Integer, ForeignKey('users.id'))
    owner = Mapped["Owner"] = relationship(back_populates='tasks')