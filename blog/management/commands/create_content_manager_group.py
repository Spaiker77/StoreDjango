from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import BlogPost


class Command(BaseCommand):
    help = 'Создает группу "Контент-менеджер" и назначает права'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(BlogPost)

        # Получаем или создаем группу
        group, created = Group.objects.get_or_create(name='Контент-менеджер')

        # Назначаем права
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=['can_publish_post', 'can_edit_any_post', 'can_delete_any_post']
        )
        group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Группа "Контент-менеджер" создана с правами!'))