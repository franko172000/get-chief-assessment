from typing import Type

from faker import Faker

from app.persistence.models import User

fake = Faker('en_US')


def generate_users(count: int) -> list[User]:
    users = []
    for i in range(count):
        users.append(User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            password=fake.password(),
            email=fake.email(),
        ))
    return users


def generate_user() -> User:
    return generate_users(1)[0]
