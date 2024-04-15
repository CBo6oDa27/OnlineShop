from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

