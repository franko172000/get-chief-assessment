from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.get('/')
def hello():
    return 'Hello World! from Auth!'
