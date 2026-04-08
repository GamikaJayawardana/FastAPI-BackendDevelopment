from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseSettings):
    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_PORT: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    
    model_config = SettingsConfigDict(
        env_file="./.env",
        env_ignore_empty=True,
        extra="ignore",
    )

settings = DatabaseSettings()
