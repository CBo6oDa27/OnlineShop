from django.core.management import (BaseCommand)

from catalog.models import Category, Product

import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data_dump.json') as file:
            data = json.load(file)
            categories = [obj for obj in data if obj.get('model') == 'catalog.category']
            return categories

    @staticmethod
    def json_read_products():
        with open('data_dump.json') as file:
            data = json.load(file)
            products = [obj for obj in data if obj.get('model') == 'catalog.product']
            return products

    def handle(self, *args, **options):
        # Очистка данных в модели Product
        Product.objects.all().delete()

        # Очистка данных в модели Catalog
        Category.objects.all().delete()


        categories_to_create = []
        products_to_create = []
        category_list = self.json_read_categories()

        for category_item in category_list:
            fields_dict = category_item['fields']
            fields_dict = {'pk': category_item['pk'], **fields_dict}
            categories_to_create.append(Category(**fields_dict))

        Category.objects.bulk_create(categories_to_create)

        products_list = self.json_read_products()
        for product_item in products_list:
            fields_dict = product_item['fields']
            fields_dict['category'] = Category.objects.get(pk=fields_dict['category'])
            products_to_create.append(Product(**fields_dict))

        Product.objects.bulk_create(products_to_create)



