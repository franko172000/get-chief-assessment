from fastapi import HTTPException
from starlette import status

from app.http.controllers.v1.auth.dto.auth_request import AuthLoginRequest
from app.persistence.reposiroties.user_repository import UserRepository
from app.services.auth.auth_token_jwt_handler import AuthJWTTokenHandler
from app.services.base_service import BaseService
from app.utils.hashing import Hash
from app.http.controllers.v1.auth.dto.auth_response import TokenResponse


class AuthService(BaseService):

    def login_user(self, data: AuthLoginRequest) -> TokenResponse:
        user_repo = UserRepository(self.db)
        user = user_repo.get_user_by_email(email=data.email)

        if not user or not Hash.verify_password(data.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')

        return AuthJWTTokenHandler.sign_jwt(user.id)

    def logout(self):
        pass
