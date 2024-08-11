from pydantic.v1 import BaseSettings


class JwtPayload(BaseSettings):
    user_id: int
    expires_in: int