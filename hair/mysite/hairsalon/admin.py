from django.contrib import admin
from .models import Item, Service, Designer, bookingItem


admin.site.register(Item)
admin.site.register(Service)
admin.site.register(Designer)
admin.site.register(bookingItem)
# Register your models here.
