from pydantic.v1 import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    ENV: str = "development"
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRES: int = os.getenv("JWT_ACCESS_TOKEN_EXPIRES")
    DATABASE_URL: str = os.getenv("DATABASE_URL")


app_config = Config()
