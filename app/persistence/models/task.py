from sqlalchemy import Integer, Column, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, relationship
from .base_model import BaseModel
from . import Base


class Task(BaseModel):
    __tablename__ = 'tasks'
    title = Column(String)
    description = Column(Text)
    status = Column(String)
    assigned_date = Column(DateTime(timezone=True), nullable=True, default=None)
    due_date = Column(DateTime(timezone=True), nullable=True, default=None)
    priority = Column(String)
    owner_id: Mapped[int] = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), nullable=True, default=None)
    owner = relationship("User", back_populates='tasks')
