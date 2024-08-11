from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import app_config

engine = create_engine(
    app_config.DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def create_tables():
#     modelBase.metadata.create_all(bind=engine)