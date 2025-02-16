from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(PizzaSize)
admin.site.register(PizzaCrust)
admin.site.register(PizzaSauce)
admin.site.register(PizzaCheese)
admin.site.register(Pizza)
admin.site.register(Order)