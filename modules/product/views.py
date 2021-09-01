from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def ProductList(request):
    p = Product.objects.all()
    return render(request, "product/product-update.html", {'p': p})
