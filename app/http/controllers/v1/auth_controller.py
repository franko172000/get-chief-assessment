from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth')


@auth_router.get('/')
def hello():
    return 'Hello World!'
