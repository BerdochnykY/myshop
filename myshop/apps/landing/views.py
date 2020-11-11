from django.shortcuts import render
from .forms import SubscriberForm
from django.http import HttpResponse



def homepage(request):
    return render(request, 'landing/homepage.html')


def landing(request):
    form = SubscriberForm(request.POST or None)
    return render(request, 'landing/landing.html')
