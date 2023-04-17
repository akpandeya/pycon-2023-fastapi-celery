from celery import Celery
from src.config import settings


def make_celery(config: dict = settings.CELERY_CONFIG):
    celery_app = Celery("tasks")
    celery_app.conf.update(config)
    return celery_app
