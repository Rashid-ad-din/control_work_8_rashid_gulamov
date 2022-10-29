from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Автор, оставивший отзыв',
        related_name='review_authors',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        to='webapp.Product',
        verbose_name='Продукт, получивший отзыв',
        related_name='reviewed_products',
        on_delete=models.CASCADE,
    )
    description = models.TextField(verbose_name='Отзыв', null=False, blank=False, max_length=2000)
    rating = models.IntegerField(
        verbose_name='Оценка',
        null=False,
        blank=False,
        validators=[
            MaxValueValidator(limit_value=5, message='Значение не может быть более 5'),
            MinValueValidator(limit_value=1, message='Значение не может быть менее 1')
        ]
    )
