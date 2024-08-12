import time
from typing import List, Type

import jwt
import pytest
from faker import Faker
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from app import app
from app.core.db.database import Base, get_db
from app.persistence.models import Task
from app.utils.hashing import Hash
from tests.mock_data import generate_users, generate_user
from app.config import app_config

fake = Faker('en_US')

# SQLite database URL for testing
SQLITE_DATABASE_URL = "sqlite:///./test_db.db"

# Create a SQLAlchemy engine
engine = create_engine(
    SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create a sessionmaker to manage sessions
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the database
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a new database session with a rollback at the end of the test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    """Create a test client that uses the override_get_db fixture to return a session."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope='function')
def fx_get_access_token():
    def _user_id(user_id):
        payload: dict = {
            "user_id": user_id,
            "expires_in": time.time() + app_config.JWT_ACCESS_TOKEN_EXPIRES
        }
        return jwt.encode(payload, app_config.JWT_SECRET_KEY, algorithm=app_config.JWT_ALGORITHM)

    return _user_id


@pytest.fixture(scope='function')
def fx_create_users(db_session):
    users = generate_users(10)
    db_session.bulk_save_objects(users)
    db_session.commit()


@pytest.fixture(scope='function')
def fx_create_user(db_session: Session) -> dict:
    user = generate_user()
    old_password = user.password
    user.password = Hash.hash_password(user.password)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return {
        'new_user': user,
        'old_password': old_password,
    }


@pytest.fixture(scope='function')
def fx_create_tasks(db_session: Session, fx_create_user) -> list[Type[Task]]:
    tasks = []
    user = fx_create_user['new_user']
    for i in range(10):
        tasks.append(Task(
            title=fake.street_name(),
            description=fake.paragraph(),
            owner_id=user.id,
            assigned_date=fake.date_time(),
            due_date=fake.date_time(),
            priority='high',
        ))
    db_session.bulk_save_objects(tasks)
    db_session.commit()

    return db_session.query(Task).all()
