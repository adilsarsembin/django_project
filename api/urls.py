from django.urls import path
from . import views

product_url = 'products/'

urlpatterns = [
    path(f'{product_url}', views.products, name='all_products'),
    path(f'{product_url}<int:pk>', views.product, name='product'),
]
