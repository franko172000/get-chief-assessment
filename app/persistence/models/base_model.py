from abc import ABC
from datetime import datetime, UTC

from sqlalchemy import Column, DateTime, Integer, func
from . import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=datetime.now(UTC))
