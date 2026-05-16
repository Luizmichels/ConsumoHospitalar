# Lê as variáveis do .env e as disponibiliza o projeto
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SUPER_ADMIN_EMAIL: str
    SUPER_ADMIN_SENHA: str

    class Config:
        env_file = ".env"


settings = Settings()
