from django.core.management.base import BaseCommand
from django.utils import timezone
from mailing.models import Mailing
from mailing.services import send_mailing


class Command(BaseCommand):
    help = "Send scheduled mailings"

    def handle(self, *args, **options):
        now = timezone.now()
        mailings = Mailing.objects.filter(
            start_time__lte=now,
            end_time__gte=now,
            status__in=[Mailing.STATUS_CREATED, Mailing.STATUS_STARTED],
        )

        for mailing in mailings:
            result = send_mailing(mailing)
            self.stdout.write(
                f"Mailing #{mailing.id}: "
                f"success={result['success']}, failure={result['failure']}"
            )
