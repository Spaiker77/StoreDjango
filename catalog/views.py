from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Product, Category, Contact
from .forms import ProductForm


class HomePageView(ListView):
    """Главная страница с товарами"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-created_at')[:12]  # Ограничим количество

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactPageView(TemplateView):
    """Контактная страница"""
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Получено новое сообщение от {name} ({phone}): {message}')
        return self.get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    """Детальная страница товара"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class AddProductView(CreateView):
    """Создание нового товара"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('home')
