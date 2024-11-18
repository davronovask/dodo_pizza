from rest_framework import serializers
from .models import Drink, Pizza

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'price', 'image', 'is_new', 'size']

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'name', 'price', 'ingredients', 'image', 'is_new', 'size', 'weight']