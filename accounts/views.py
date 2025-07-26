
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserLoginForm
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.conf import settings
from .forms import UserRegisterForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        # Автовход
        login(self.request, user)

        # Отправка письма
        try:
            self.send_welcome_email(user)
            messages.success(
                self.request,
                f'Регистрация прошла успешно! На {user.email} отправлено письмо.'
            )
        except Exception as e:
            messages.error(
                self.request,
                'Регистрация прошла успешно, но не удалось отправить письмо.'
            )
            # Логируем ошибку
            print(f"Ошибка отправки письма: {e}")

        return response

    def send_welcome_email(self, user):
        subject = 'Добро пожаловать в наш магазин!'
        html_message = render_to_string(
            'accounts/email/welcome.html',
            {'user': user, 'site_url': self.request.build_absolute_uri('/')}
        )
        plain_message = strip_tags(html_message)

        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html_message,
            fail_silently=False,
        )

class LoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'avatar', 'phone', 'country']
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлен')
        return super().form_valid(form)