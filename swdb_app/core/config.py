import os
from pydantic_settings import BaseSettings

ENV = os.getenv("ENV", "development")


class Settings(BaseSettings):
    SYNC_DB_URL: str
    ASYNC_DB_URL: str

    class Config:
        env_file = ".env" if ENV == "development" else None


settings = Settings()
