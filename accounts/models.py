from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Кастомный менеджер для модели User с email"""

    def create_user(self, email, password=None, **extra_fields):
        """Создает и сохраняет пользователя с email и паролем"""
        if not email:
            raise ValueError('Пользователь должен иметь email адрес')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает и сохраняет суперпользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    # Убираем стандартное поле username
    username = None

    # Делаем email уникальным полем для авторизации
    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text='Обязательное поле. Введите действующий email адрес.'
    )

    avatar = models.ImageField(
        upload_to='users/avatars/',
        verbose_name='Аватар профиля',
        null=True,
        blank=True,
        help_text='Загрузите изображение вашего профиля'
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        null=True,
        blank=True,
        help_text='Введите номер в формате +79991234567'
    )

    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        null=True,
        blank=True,
        help_text='Укажите вашу страну проживания'
    )

    # Указываем email как поле для авторизации
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Указываем кастомный менеджер
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email