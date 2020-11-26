from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def product(request, product_id):
    product = Product.objects.get(id=product_id)

#Ключ сессии для отображения всех елементов, которые добавляются в корзину
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)


    return render(request, 'products/product.html', locals())
