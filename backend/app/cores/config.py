import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = "HS256"
    # 60 minutes * 24 hours * 7 days = 7 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    MONGO_DATABASE_URL = os.getenv('ME_CONFIG_MONGODB_URL')
    MONGO_COLLECTION_NAME = "programs"
    # Database connection
    SQLALCHEMY_DATABASE_URL = os.getenv('MYSQL_URL')
    class Config:
        case_sensitive = True


settings = Settings()
