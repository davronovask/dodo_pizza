"""
URL configuration for dodo_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from products.views import DrinkListView, DrinkDetailView, PizzaListView, PizzaDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drinks/', DrinkListView.as_view(), name='drink_list'),  # Эндпоинт для списка напитков
    path('api/v1/drinks/<int:pk>/', DrinkDetailView.as_view(), name='drink_detail'),  # Эндпоинт для детальной страницы напитка
    path('api/v1/pizzas/', PizzaListView.as_view(), name='pizza_list'),  # Эндпоинт для списка пицц
    path('api/v1/pizzas/<int:pk>/', PizzaDetailView.as_view(), name='pizza_detail'),  # Эндпоинт для детальной страницы пиццы
]
