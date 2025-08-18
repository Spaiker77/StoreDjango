from django.urls import path
from .views import (
    HomePageView,
    ContactPageView,
    ProductDetailView,
    AddProductView,
    ProductUpdateView,
    ProductDeleteView,
)
from catalog.views import unpublish_product
from .views import CategoryProductsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("add-product/", AddProductView.as_view(), name="add_product"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("product/<int:pk>/unpublish/", unpublish_product, name="product_unpublish"),
    path(
        "category/<int:category_id>/",
        CategoryProductsView.as_view(),
        name="category_products",
    ),
]
