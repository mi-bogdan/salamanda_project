from django.db import models
from django.contrib.auth.models import User
from news.models import Post


class Profile(models.Model):
    """Профиль пользователя"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    voted_for = models.ManyToManyField(
        Post, verbose_name='Проголосовали за', blank=True, null=True, related_name='voted_for')
    voted_against = models.ManyToManyField(
        Post, verbose_name='Проголосовали против', blank=True, null=True, related_name='voted_against')
    save_post = models.ManyToManyField(
        Post, verbose_name='Сохраненные', blank=True, null=True, related_name='save_post')
    img_profile = models.ImageField(
        verbose_name="Фото_профиля", upload_to='profile/%Y/%m/%d', blank=True, null=True)
    key_words = models.TextField(verbose_name='Ключи_рекомендаций', blank=True)

    def __str__(self) -> str:
        return f'{self.user}'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
