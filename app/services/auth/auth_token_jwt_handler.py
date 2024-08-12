import time
from typing import Union

import jwt

from app.config import app_config
from app.http.controllers.v1.auth.dto.auth_response import TokenResponse


class AuthJWTTokenHandler:
    @staticmethod
    def decode_jwt(token: str) -> Union[dict, None]:
        try:
            decoded_token = jwt.decode(token, app_config.JWT_SECRET_KEY, algorithms=[app_config.JWT_ALGORITHM])
            return decoded_token if decoded_token["expires_in"] >= time.time() else None
        except:
            return None

    @staticmethod
    def sign_jwt(user_id: int) -> TokenResponse:
        payload: dict = {
            "user_id": user_id,
            "expires_in": time.time() + app_config.JWT_ACCESS_TOKEN_EXPIRES
        }
        token = jwt.encode(payload, app_config.JWT_SECRET_KEY, algorithm=app_config.JWT_ALGORITHM)
        return TokenResponse(access_token=token, token_type="Bearer")
