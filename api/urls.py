from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='all_products'),
    path('<int:pk>', views.product, name='product'),
]
