from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(help_text='указывайте цену в сомах')
    ingredients = models.TextField()
    image = models.ImageField(upload_to='pizza_images/')
    is_new = models.BooleanField(default=False)  # Флаг для новинок
    size = models.PositiveIntegerField()
    weight = models.PositiveIntegerField(verbose_name='вес в граммах')

class Meta:
    verbose_name_plural = 'Пиццы'
    verbose_name = 'Пицца'

class Drink(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(help_text='Укажите цену в сомах')
    image = models.ImageField(upload_to='drink_images/')
    is_new = models.BooleanField(default=False)  # Флаг для новинок
    size = models.DecimalField(
        max_digits=3, decimal_places=2,
        help_text='Размер напитка в литрах (например, 0.33 для 330 мл)',
    )

    class Meta:
        verbose_name_plural = 'Напитки'
        verbose_name = 'Напиток'
