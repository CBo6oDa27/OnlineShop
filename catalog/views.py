from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from catalog.models import Product, Version
from django.urls import reverse_lazy
from catalog.forms import ProductForm, ProductModeratorForm, VersionForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            current_versions = versions.filter(is_current=True)
            if current_versions:
                product.name_version = current_versions.last().name
                product.number_version = current_versions.last().number
                print(product.number_version)
                print(product.name_version)
        context_data['object_list'] = products
        return context_data


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif (user.has_perm('catalog.can_edit_publication_status')
              and user.has_perm('catalog.can_edit_description')
              and user.has_perm('catalog.can_change_category')):
            return ProductModeratorForm
        else:
            raise PermissionDenied


class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):
        return Version.objects.filter(product=Product.objects.get(pk=self.kwargs.get('pk')))


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')

    def get_success_url(self):
        product = self.object.product
        return reverse_lazy('catalog:product', kwargs={'pk': product.pk})


class VersionDetailView(DetailView):
    model = Version
    context_object_name = 'versions'
