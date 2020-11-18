from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('product/<int:product_id>/', views.product, name='product'),
]
