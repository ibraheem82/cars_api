from django.contrib import admin
from .models import Order
# Register your models here.
# * Register this for customization
@admin.register(Order)
# * Everytime we want to create our custom 

class OrderAdmin(admin.ModelAdmin):
    # * list of things you want to display.
    list_display = ['brand', 'order_status', 'quantity', 'created_at']
    # * filtering in the {django} administration
    list_filter  = ['created_at', 'order_status', 'brand']