from pythondi import Provider, configure

from app.persistence.reposiroties.user_repository import UserRepository


def init_di():
    provider = Provider()
    provider.bind(UserRepository)
    configure(provider=provider)