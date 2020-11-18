from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'products/product.html', locals())
