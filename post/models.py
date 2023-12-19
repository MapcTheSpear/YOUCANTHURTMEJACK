"""
models.py - для таблиц
"""

from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='posts/media', null=True, blank=False)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} {self.rate}"

    class Meta:
        db_table = 'post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Products(models.Model):
    image = models.ImageField(upload_to='posts/media', null=True, blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
