from typing import List

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship
from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    tasks= relationship("Task", back_populates='owner')
