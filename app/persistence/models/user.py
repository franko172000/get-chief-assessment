from datetime import datetime, UTC
from typing import List

from sqlalchemy import BaseModel, Integer, Column, String, DateTime, relationship
from sqlalchemy.orm import Mapped

from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    name = Column(String)
    email = Column(String)
    password = Column(String)
    tasks: Mapped[List["Task"]] = relationship(back_populates='owner')
