from django.shortcuts import render
from .models import Product, Category, Contact


def home(request):
    """Главная страница с последними товарами и категориями"""
    latest_products = Product.objects.order_by('-created_at')[:5]
    categories = Category.objects.all()

    context = {
        'products': latest_products,
        'categories': categories,
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Страница контактов с формой обратной связи"""
    contact_info = Contact.objects.first()  # Получаем первый контакт из БД

    if request.method == 'POST':
        # Обработка данных формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Получено новое сообщение от {name} ({phone}): {message}')

    context = {
        'contact': contact_info,
        'categories': Category.objects.all(),  # Для отображения в навигации
    }
    return render(request, 'catalog/contacts.html', context)