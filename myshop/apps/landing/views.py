from django.shortcuts import render, redirect
from .forms import SubscriberForm
from django.http import HttpResponse
from .models import Subscriber
from products.models import *



def homepage(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_shi = products_images.filter(product__type__id=2)
    products_images_zap = products_images.filter(product__type__id=1)

    return render(request, 'landing/homepage.html', locals())






def landing(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = SubscriberForm()
    context = {
        'form': form
    }
    subscribers = Subscriber.objects.all()
    return render(request, 'landing/landing.html', context)
