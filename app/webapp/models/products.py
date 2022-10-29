from django.db import models
from django.db.models import TextChoices


class CategoryChoices(TextChoices):
    ELECTRONICS = 'electronics', 'Электроника'
    CARS = 'cars', 'Автомобили'
    DRONES = 'drones', 'Дроны'


class Product(models.Model):
    title = models.CharField(verbose_name='Продукт', null=False, blank=False, max_length=150)
    category = models.CharField(
        verbose_name='Категория',
        null=False,
        blank=False,
        choices=CategoryChoices.choices,
        max_length=150
    )
    description = models.TextField(verbose_name='Описание', null=True, blank=True, max_length=2000)
    image = models.ImageField(
        verbose_name='Фото продукта',
        null=True,
        blank=True,
        upload_to='avatars'
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
