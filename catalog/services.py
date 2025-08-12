from django.core.cache import cache
from django.forms.models import model_to_dict
from .models import Product
import json


def get_products_by_category(category_id):
    cache_key = f"products_category_{category_id}"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return [Product(**item) for item in json.loads(cached_data)]

    products = list(
        Product.objects.filter(
            category_id=category_id, status="published"
        ).select_related("category")
    )

    if products:
        serialized = json.dumps([model_to_dict(p) for p in products])
        cache.set(cache_key, serialized, 60 * 60)

    return products
