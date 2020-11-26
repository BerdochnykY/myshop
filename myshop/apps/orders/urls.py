from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('basket_adding/', views.basket_adding, name='basket_adding'),
]
