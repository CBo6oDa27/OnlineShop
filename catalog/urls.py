from django.urls import path
from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView, ProductCreateView, ProductUpdateView, VersionCreateView, VersionListView, VersionUpdateView, VersionDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('version/', VersionCreateView.as_view(), name='create_version'),
    path('versions/<int:pk>', VersionListView.as_view(), name='versions'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='update_version'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='version_detail')
]
