from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Ip(models.Model):  # наша таблица где будут айпи адреса
    """Айпи адреса"""
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Tags(models.Model):
    """Теги"""
    title = models.CharField(verbose_name="Название", max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Посты новостей"""

    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(
        User, verbose_name='автор', related_name='author', null=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True)
    update_at = models.DateTimeField(
        verbose_name="Дата публикации", auto_now=True)
    photo = models.ImageField(
        verbose_name="Фото", upload_to='photo/%Y/%m/%d', blank=True)
    published = models.BooleanField(
        verbose_name="ПубликованаЛИ", default=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=160, unique=True)
    voting = models.IntegerField(
        verbose_name='Голосование', blank=True, null=True, default=0)
    views = models.ManyToManyField(
        Ip, related_name="post_views", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Review(models.Model):
    """Отзывы"""
    user = models.ForeignKey(
        User, verbose_name='пользователь', on_delete=models.PROTECT)
    text = models.TextField(verbose_name="Отписание", max_length=5000)
    perents = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    post = models.ForeignKey(
        Post, verbose_name="Пост", on_delete=models.CASCADE, related_name='review')

    def __str__(self) -> str:
        return f'{self.post}-{self.user}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



