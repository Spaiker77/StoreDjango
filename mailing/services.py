from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import MailingAttempt, Mailing
import logging

logger = logging.getLogger(__name__)


def send_mailing(mailing):
    """
    Отправляет рассылку и сохраняет попытку отправки
    Возвращает словарь с результатами: {'success': int, 'failure': int}
    """
    # Проверяем, что рассылка активна
    now = timezone.now()
    if mailing.end_time < now:
        mailing.status = Mailing.STATUS_COMPLETED
        mailing.save()
        logger.info(f"Рассылка {mailing.id} уже завершена")
        return {"success": 0, "failure": 0}

    success_count = 0
    failure_count = 0

    for client in mailing.clients.all():
        try:
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[client.email],
                fail_silently=False,
            )
            status = MailingAttempt.STATUS_SUCCESS
            response = "Успешно отправлено"
            success_count += 1
            logger.info(f"Письмо для {client.email} отправлено успешно")
        except Exception as e:
            status = MailingAttempt.STATUS_FAILURE
            response = str(e)
            failure_count += 1
            logger.error(f"Ошибка отправки для {client.email}: {str(e)}")

        MailingAttempt.objects.create(
            mailing=mailing, status=status, server_response=response
        )

    # Обновляем статус рассылки
    if success_count > 0:
        mailing.status = Mailing.STATUS_STARTED
    elif mailing.status == Mailing.STATUS_CREATED:
        mailing.status = Mailing.STATUS_STARTED  # Хотя бы одна попытка была

    mailing.save()

    logger.info(
        f"Рассылка {mailing.id} завершена. "
        f"Успешно: {success_count}, Неудачно: {failure_count}"
    )

    return {"success": success_count, "failure": failure_count}
