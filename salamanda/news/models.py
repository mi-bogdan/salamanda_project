from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User


class Ip(models.Model):  # наша таблица где будут айпи адреса
    """Айпи адреса"""
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Tags(models.Model):
    """Теги"""
    title = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Communities(models.Model):
    """Сообщества"""
    title = models.CharField(verbose_name='Сообщество',
                             unique=True, max_length=255)
    description = models.TextField(verbose_name="Описание")
    create_at = models.DateTimeField(
        verbose_name='Дата_публикации', auto_now_add=True)
    img = models.ImageField(
        verbose_name='Изображение_сообщества', upload_to='communities/%Y/%m/%d', blank=True)
    admin_communities = models.OneToOneField(
        User, verbose_name='Админ_сообщества', on_delete=models.CASCADE, related_name='admin')
    user_in_communities = models.ManyToManyField(
        User, verbose_name='Пользователи_сообщества', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"

    def save(self, *args, **kwargs):
        self.title = 'r/' + self.title
        return super(Communities, self).save(*args, **kwargs)


class Post(models.Model):
    """Посты новостей"""

    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(
        User, verbose_name='автор', related_name='author', null=True, on_delete=models.CASCADE)
    сommunities = models.ForeignKey(
        Communities, verbose_name='Сообщества', on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(
        verbose_name='Дата_публикации', auto_now_add=True)
    update_at = models.DateTimeField(
        verbose_name='Дата_обновления', auto_now=True)
    photo = models.ImageField(
        verbose_name='Фото', upload_to='photo/%Y/%m/%d', blank=True)
    published = models.BooleanField(
        verbose_name='ПубликованаЛИ', default=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=160, unique=True)
    voting = models.IntegerField(
        verbose_name='Голосование', blank=True, null=True, default=0)
    views = models.ManyToManyField(
        Ip, related_name='post_views', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Review(models.Model):
    """Отзывы"""
    user = models.ForeignKey(
        User, verbose_name='пользователь', on_delete=models.PROTECT)
    text = models.TextField(verbose_name='Описание', max_length=5000)
    perents = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    post = models.ForeignKey(
        Post, verbose_name='Пост', on_delete=models.CASCADE, related_name='review')

    def __str__(self) -> str:
        return f'{self.post}-{self.user}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
