from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ARMOR Main Backend API"
    app_version: str = "0.1.0"

    database_url: str = ""

    ai_service_url: str = "http://localhost:8001"
    ai_service_timeout: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()