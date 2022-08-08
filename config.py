from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    SQLALCHEMY_DATABASE_URI: PostgresDsn = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_SERVER'),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    @validator('PASSWORD', pre=True)
    def check_password_len(cls, password: Optional[str]):
        if len(password)<3:
            raise ValueError('Пароль слишком короткий')
        return password

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()