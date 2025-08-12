from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .models import Product, Category, Contact
from .forms import ProductForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import get_products_by_category


@permission_required("catalog.can_unpublish_product", raise_exception=True)
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.status = "draft"
    product.save()
    messages.success(request, f'Публикация продукта "{product.name}" отменена.')
    return redirect("product_detail", pk=pk)


class HomePageView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    queryset = Product.objects.order_by("-created_at")[:12]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ContactPageView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.first()
        context["categories"] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        print(
            f"Новое сообщение от {request.POST.get('name')} ({request.POST.get('phone')}): {request.POST.get('message')}"
        )
        return self.get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"

    @method_decorator(cache_page(60 * 15))  # Кешируем на 15 минут
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = self.object
        context["can_edit"] = False
        if user.is_authenticated:
            if (
                product.owner == user
                or user.groups.filter(name="Модератор продуктов").exists()
            ):
                context["can_edit"] = True
        return context


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = "draft"
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user:
            raise Http404("Вы не являетесь владельцем этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = request.user.groups.filter(name="Модератор продуктов").exists()
        if not (is_owner or is_moderator):
            raise Http404("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class CategoryProductsView(ListView):
    template_name = "catalog/category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(id=self.kwargs["category_id"])
        return context
