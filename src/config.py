from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PROJECT_NAME = "flask celey tdd"
    PRODUCT_SERVICE_URL = Field(default="http://localhost:8081/product")
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"

    CELERY_CONFIG = {
        "broker_url": CELERY_BROKER_URL,
        "result_backend": CELERY_RESULT_BACKEND,
    }


settings = Settings()
