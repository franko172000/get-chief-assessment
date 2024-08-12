import pytest

from app.services.auth.auth_token_jwt_handler import AuthJWTTokenHandler
from app.services.user_service import UserService
from app.utils.hashing import Hash
from tests.mock_data import generate_users, generate_user


@pytest.fixture(scope='function')
def fx_get_access_token(user_id):
    return AuthJWTTokenHandler.sign_jwt(user_id)


@pytest.fixture(scope='function')
def fx_create_users(db_session):
    users = generate_users(10)
    db_session.bulk_save_objects(users)
    db_session.commit()


@pytest.fixture(scope='function')
def fx_create_user(db_session):
    user = generate_user()
    user.password = Hash.hash_password(user.password)
    db_session.bulk_save_objects(user)
    db_session.commit()
    return user
