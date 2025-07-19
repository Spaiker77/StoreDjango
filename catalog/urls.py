from django.urls import path
from .views import (
    HomePageView, ContactPageView, ProductDetailView,
    AddProductView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add-product/', AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
]
