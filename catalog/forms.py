from django import forms
from django.core.exceptions import ValidationError
from .models import Product

# 🔒 Список запрещённых слов (переиспользуемый)
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    # 🎨 Стилизация формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control-file'

    # 🧼 Валидация: запрет слов в названии
    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Название содержит запрещённое слово: «{word}»")
        return name

    # 🧼 Валидация: запрет слов в описании
    def clean_description(self):
        description = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Описание содержит запрещённое слово: «{word}»")
        return description

    # 💰 Валидация: цена не может быть отрицательной
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    # 🖼️ Валидация: изображение — только JPG/PNG и ≤ 5MB
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер изображения не должен превышать 5 МБ.")
            if not image.content_type in ['image/jpeg', 'image/png']:
                raise ValidationError("Допустимы только изображения JPEG или PNG.")
        return image
