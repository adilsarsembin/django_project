from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),  
    path('auth/', include('djoser.urls.jwt')),
    path('products/', include('api.urls')),
]
