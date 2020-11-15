from .models import *
from django.forms import ModelForm, TextInput, EmailInput

#class SubscriberForm(ModelForm):
#
#    class Meta:
#        model = Subscriber
#        exclude = [""]
#        widgets = {
#            "sub_name": TextInput(attrs={
#                'class': 'form-control',
#                'placeholder': 'Введите имя'
#            }),
#            "sub_email": EmailInput(attrs={
#                'class': 'form-control',
#                'placeholder': 'Введите емейл'
#            }),
#        }
