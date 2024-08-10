from datetime import datetime, UTC

from sqlalchemy import Column, DateTime, Integer, func

from app.config.database import Base


class BaseModel(Base):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=datetime.now(UTC))
