from typing import List

from sqlalchemy import Column, String, Integer, func, select
from sqlalchemy.orm import Mapped, relationship, column_property
from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    tasks = relationship("Task", back_populates='owner')
    # tasks_count = column_property(
    #     select(func.count(tasks.t.owner_id)).filter(tasks.t.owner_id == id).scalar_subquery(),
    #     deferred=True,
    # )
