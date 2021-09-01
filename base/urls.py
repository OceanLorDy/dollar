from django.urls import path, include
from . import views

urlpatterns = [
    path("", include('modules.authentication.urls')),
    path("product/", include('modules.product.urls')),
]
