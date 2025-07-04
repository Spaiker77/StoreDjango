from django.core.management.base import BaseCommand
from catalog.models import Product, Category
import json

class Command(BaseCommand):
    help = 'Fill database with test products'

    def handle(self, *args, **options):
        # Удаление старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка фикстур
        with open('catalog/fixtures/category.json', 'r') as f:
            categories = json.load(f)
            for cat in categories:
                Category.objects.create(
                    pk=cat['pk'],
                    name=cat['fields']['name'],
                    description=cat['fields']['description']
                )

        with open('catalog/fixtures/product.json', 'r') as f:
            products = json.load(f)
            for prod in products:
                Product.objects.create(
                    pk=prod['pk'],
                    name=prod['fields']['name'],
                    description=prod['fields']['description'],
                    category_id=prod['fields']['category'],
                    price=prod['fields']['price']
                )

        self.stdout.write(self.style.SUCCESS('Successfully filled database'))