from django.contrib import admin
from .models import Pizza, Drink

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Drink)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name']
