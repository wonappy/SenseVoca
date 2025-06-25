# core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    dalle_api_key: str
    stt_api_key: str

    class Config:
        env_file = ".env"   # 기본 경로 설정 (.env에서 불러옴)


settings = Settings()