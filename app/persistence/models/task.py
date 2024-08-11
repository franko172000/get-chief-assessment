from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from .base_model import BaseModel
from . import Base


class Task(BaseModel):
    __tablename__ = 'tasks'
    title = Column(String)
    description = Column(String)
    status = Column(String)
    owner_id: Mapped[int] = Column(Integer, ForeignKey('users.id'), nullable=True, default=None)
    owner = relationship("User", back_populates='tasks')