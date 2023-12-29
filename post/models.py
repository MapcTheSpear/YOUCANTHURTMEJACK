"""
models.py - для таблиц
"""

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class Hashtag(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'hashtag'
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


class Post(BaseModel):
    image = models.ImageField(upload_to='posts/media', null=True, blank=False)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    hashtags = models.ManyToManyField(
        Hashtag,
        verbose_name='Хэштеги',
        related_name="posts"
    )

    def __str__(self) -> str:
        return f"{self.title} {self.rate}"

    class Meta:
        db_table = 'post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


# class PostInfo(BaseModel):
#     post = models.OneToOneField(
#         Post,
#         on_delete=models.CASCADE,
#         verbose_name='Пост',
#         related_name='info'
#     )
#     likes = models.IntegerField(default=0, verbose_name='Лайки')
#     dislikes = models.IntegerField(default=0, verbose_name='Дизлайки')
#
#     def __str__(self) -> str:
#         return f'{self.likes} {self.dislikes}'
#
#     class Meta:
#         db_table = 'post_info'
#         verbose_name = 'Информация поста'
#         verbose_name_plural = 'Информация постов'


class Category(BaseModel):
    type = models.TextField(null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.type}'

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(BaseModel):
    image = models.ImageField(upload_to='posts/', null=True, blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    category = models.ManyToManyField(
        Category,
        verbose_name='Категории',
        related_name="category"
    )

    def __str__(self) -> str:
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-price']


# class PostHastags(BaseModel):
#     post = models.ForeignKey(
#         Post,
#         on_delete=models.CASCADE,
#         verbose_name='Пост',
#         related_name='hashtags'
#     )
#     hashtag = models.ForeignKey(
#         Hashtag,
#         on_delete=models.CASCADE,
#         verbose_name='Хэштег',
#         related_name='posts'
#     )
#     date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#
#     def __str__(self) -> str:
#         return f'{self.post} {self.hashtag}'


class Comments(BaseModel):
    post = models.ForeignKey(
        "post.Post",
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='comments'
    )
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Review(BaseModel):
    product = models.ForeignKey(
        "post.Products",
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        related_name='reviews'
    )
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



