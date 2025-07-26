from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Category, Contact
from .forms import ProductForm

class HomePageView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-created_at')[:12]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        print(f"Новое сообщение от {request.POST.get('name')} ({request.POST.get('phone')}): {request.POST.get('message')}")
        return self.get(request, *args, **kwargs)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')
