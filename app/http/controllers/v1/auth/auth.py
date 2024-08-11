from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.database import get_db
from app.http.controllers.v1.auth.dto.auth_request import AuthLoginRequest
from app.http.controllers.v1.auth.dto.auth_response import TokenResponse
from app.services.auth.auth_service import AuthService

auth_router = APIRouter()


@auth_router.post('/login', response_model=TokenResponse)
def login(request: AuthLoginRequest, db: Session = Depends(get_db)):
    return AuthService(db).login_user(request)
