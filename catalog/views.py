from .models import Product, Category, Contact
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm

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

def product_detail(request, pk):
    """Контроллер для страницы товара"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def home(request):
    """Главная страница с товарами"""
    products = Product.objects.order_by('-created_at')[:12]  # Ограничиваем количество
    return render(request, 'catalog/home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'catalog/add_product.html', {'form': form})