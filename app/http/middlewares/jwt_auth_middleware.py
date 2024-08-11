from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from starlette import status

from app.services.auth.auth_token_jwt_handler import AuthJWTTokenHandler


class JWTAuthMiddleware(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTAuthMiddleware, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTAuthMiddleware, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                self.throw_authentication_error("Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                self.throw_authentication_error("Invalid token or expired token.")
            return credentials.credentials
        else:
            self.throw_authentication_error("Invalid authorization code.")

    def verify_jwt(self, jwt_token: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = AuthJWTTokenHandler.decode_jwt(jwt_token)
        except:
            payload = None
        if payload:
            is_token_valid = True

        return is_token_valid

    def throw_authentication_error(self, message: str = "Invalid authorization code."):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message,
            headers={"WWW-Authenticate": "Bearer"},
        )
