from celery import shared_task
from src.service import EmailService


@shared_task
def send_email_task(to_email: str, message: str):
    email_service = EmailService()
    email_service.send_email(to_email, message)
