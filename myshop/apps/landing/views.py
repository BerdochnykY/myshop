from django.shortcuts import render, redirect
from .forms import SubscriberForm
from django.http import HttpResponse
from .models import Subscriber



def homepage(request):
    return render(request, 'landing/homepage.html')


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
    return render(request, 'landing/landing0.html', context)
