from django.db import models
from django.conf import settings
from django.utils import timezone


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        permissions = [
            ("view_all_clients", "Может просматривать всех клиентов"),
        ]

    def __str__(self):
        return self.full_name


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        permissions = [
            ("view_all_messages", "Может просматривать все сообщения"),
        ]

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CREATED = "created"
    STATUS_STARTED = "started"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = [
        (STATUS_CREATED, "Создана"),
        (STATUS_STARTED, "Запущена"),
        (STATUS_COMPLETED, "Завершена"),
    ]

    start_time = models.DateTimeField(verbose_name="Время начала")
    end_time = models.DateTimeField(verbose_name="Время окончания")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED,
        verbose_name="Статус",
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Сообщение"
    )
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ("view_all_mailings", "Может просматривать все рассылки"),
            ("disable_mailing", "Может отключать рассылки"),
        ]
        ordering = ["-start_time"]

    def __str__(self):
        return f"Рассылка #{self.pk}"

    @property
    def is_active(self):
        now = timezone.now()
        return (
            self.start_time <= now <= self.end_time
            and self.status == self.STATUS_STARTED
        )


class MailingAttempt(models.Model):
    STATUS_SUCCESS = "success"
    STATUS_FAILURE = "failure"

    STATUS_CHOICES = [
        (STATUS_SUCCESS, "Успешно"),
        (STATUS_FAILURE, "Не успешно"),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True, verbose_name="Время попытки")
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, verbose_name="Статус"
    )
    server_response = models.TextField(blank=True, verbose_name="Ответ сервера")
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name="attempts",
        verbose_name="Рассылка",
    )

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
        ordering = ["-attempt_time"]

    def __str__(self):
        return f"Попытка #{self.pk} ({self.status})"
