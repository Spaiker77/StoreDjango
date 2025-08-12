from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from mailing.services import send_mailing
from mailing.models import Mailing
from django.utils import timezone


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    def send_scheduled_mailings():
        now = timezone.now()
        mailings = Mailing.objects.filter(
            start_time__lte=now, end_time__gte=now, status__in=["created", "started"]
        )
        for mailing in mailings:
            send_mailing(mailing)

    scheduler.add_job(
        send_scheduled_mailings,
        "interval",
        minutes=1,
        id="send_mailings",
        replace_existing=True,
    )

    scheduler.start()
