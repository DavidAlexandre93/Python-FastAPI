from pydantic import BaseSettings
from typing import List
from sqlalchemy.ext.declarative import declarative_base


class settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://geek:university@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = ''
    """
    realizar no interpretador do python:
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS2456'
    # 60 minutos * 24 horas * 7 dias = 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings = Setting = settings()
