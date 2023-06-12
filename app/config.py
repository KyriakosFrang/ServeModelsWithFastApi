from pydantic import BaseSettings


class AppConfig(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = False
    DATABASE_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    API_KEY: str

    class Config:
        env_file = ".env"  # Optional: Load settings from an environment file


config = AppConfig()  # type: ignore
