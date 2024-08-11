from enum import Enum

from pydantic import BaseModel


class TokenType(str, Enum):
    bearer = "Bearer"
    token = "Token"


class TokenResponse(BaseModel):
    access_token: str
    token_type: TokenType
