from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "example@mail.com",
                "autocomplete": "email",
            }
        ),
        help_text="На этот email придет письмо с подтверждением",
    )

    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+79991234567"}
        ),
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Номер должен быть в формате: '+79991234567'",
            )
        ],
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "phone", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует")
        return email


class UserLoginForm(AuthenticationForm):
    # Переопределяем стандартное поле username для использования email
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "example@mail.com"}
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Введите пароль"}
        ),
    )

    error_messages = {
        "invalid_login": "Пожалуйста, введите правильные email и пароль.",
        "inactive": "Этот аккаунт неактивен.",
    }


class ProfileUpdateForm(forms.ModelForm):
    # Форма для редактирования профиля
    class Meta:
        model = User
        fields = ("first_name", "last_name", "avatar", "phone", "country")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "+79991234567"}
            ),
            "country": forms.TextInput(attrs={"class": "form-control"}),
        }
        help_texts = {
            "avatar": "Загрузите изображение для вашего профиля",
            "phone": "В формате +79991234567",
        }
