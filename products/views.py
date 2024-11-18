from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Drink, Pizza
from .serializers import DrinkSerializer, PizzaSerializer


class DrinkListView(APIView):
    def get(self, request, *args, **kwargs):
        drinks = Drink.objects.all()
        # Сериализуем напитки
        serializer = DrinkSerializer(drinks, many=True)
        # Возвращаем сериализованные данные
        return Response(serializer.data)


# Представление для детальной страницы напитка
class DrinkDetailView(APIView):
    def get(self, request, *args, **kwargs):
        # Получаем напиток по его ID (pk)
        try:
            drink = Drink.objects.get(pk=kwargs['pk'])  # Доступ к pk из URL
        except Drink.DoesNotExist:
            return Response({'detail': 'Напиток не найден'}, status=status.HTTP_404_NOT_FOUND)

        # Сериализуем напиток
        serializer = DrinkSerializer(drink)
        # Возвращаем данные напитка
        return Response(serializer.data)


class PizzaListView(APIView):
    def get(self, request, *args, **kwargs):
        # Получаем все пиццы
        pizzas = Pizza.objects.all()
        # Сериализуем список пицц
        serializer = PizzaSerializer(pizzas, many=True)
        # Возвращаем список пицц в формате JSON
        return Response(serializer.data)


# Представление для детальной страницы пиццы
class PizzaDetailView(APIView):
    def get(self, request, *args, **kwargs):
        # Получаем пиццу по ID
        try:
            pizza = Pizza.objects.get(pk=kwargs['pk'])  # Доступ к pk из URL
        except Pizza.DoesNotExist:
            return Response({'detail': 'Пицца не найдена'}, status=status.HTTP_404_NOT_FOUND)

        # Сериализуем пиццу
        serializer = PizzaSerializer(pizza)
        # Возвращаем данные пиццы в формате JSON
        return Response(serializer.data)
