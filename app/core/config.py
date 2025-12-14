import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Cloud Backend Infra")
    ENV = os.getenv("ENV", "development")

settings = Settings()
