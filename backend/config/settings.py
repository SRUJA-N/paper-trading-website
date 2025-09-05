# config/settings.py
import json
from typing import List, Union
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "your-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Can be string (single origin), JSON string, or list
    ALLOWED_ORIGINS: Union[str, List[str]] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5431"
    POSTGRES_DB: str = "app_db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def allowed_origins_list(self) -> List[str]:
        """
        Always return ALLOWED_ORIGINS as a list, regardless of how it's defined.
        Supports:
          - JSON array (["url1","url2"])
          - Comma-separated string (url1,url2)
          - Single string (url1)
          - Already a Python list
        """
        if isinstance(self.ALLOWED_ORIGINS, list):
            return self.ALLOWED_ORIGINS

        # Try JSON decode first
        try:
            decoded = json.loads(self.ALLOWED_ORIGINS)
            if isinstance(decoded, list):
                return decoded
        except Exception:
            pass

        # Fallback: split by comma if multiple origins
        if isinstance(self.ALLOWED_ORIGINS, str):
            return [o.strip() for o in self.ALLOWED_ORIGINS.split(",") if o.strip()]

        return ["*"]  # default fallback


settings = Settings()
