from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    # Поля, которые будут отображаться в списке пользователей
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

    # Поля, которые будут отображаться в форме редактирования пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Личные данные'), {'fields': ('avatar', 'phone', 'country')}),
        (_('Права доступа'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Важные даты'), {'fields': ('last_login', 'date_joined')}),
    )

    # Поля, которые будут отображаться в форме создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
