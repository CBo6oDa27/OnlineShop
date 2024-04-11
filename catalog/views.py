from django.shortcuts import render

from catalog.models import Product

# Create your views here.


def index(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, "catalog/product.html", context)
