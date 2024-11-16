from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Literal
from pydantic import BaseModel, Field, PostgresDsn

class AppSettings(BaseModel):
    debug: bool = True
    version: str = "1.0.0"
    class Config:
        env_prefix = 'APP_'

class CorsSettings(BaseModel):
    origins: list[str] = Field(default=['*'])
    allow_credentials: bool = Field(default=True)
    allow_methods: list[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    allow_headers: list[str] = ["Authorization", "Content-Type"]
    class Config:
        env_prefix = 'CORS_'

class DatabaseSettings(BaseModel):
    dsn: PostgresDsn = Field(default="postgresql://user:password@localhost:5432/defaultdb")
    max_size: int = Field(default=64)
    min_size: int = Field(default=5)
    class Config:
        env_prefix = 'DATABASE_'

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=('.env', '.env.prod'), env_file_encoding='utf-8', extra='ignore', env_nested_delimiter="__",)
    env: Literal["development", "production"] = Field(default='development')
    app: AppSettings = AppSettings()
    cors: CorsSettings = CorsSettings()
    database: DatabaseSettings = DatabaseSettings()

settings = Settings()

@lru_cache
def get_settings():
    return Settings()
