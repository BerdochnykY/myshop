from django.urls import path

from . import views

app_name = 'landing'
urlpatterns = [
    path('home/', views.homepage),
    path('', views.landing),
]
