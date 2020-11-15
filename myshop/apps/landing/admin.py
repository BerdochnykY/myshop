from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["sub_name", "sub_email"]
    exclude = [""]
    list_filter = ["sub_name"]
    search_fields = ["sub_name", "sub_email"]
    
    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
