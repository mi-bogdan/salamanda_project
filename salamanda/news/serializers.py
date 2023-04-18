from rest_framework import serializers
from .models import Post, Ip, Tags, Review, Profile


class PostListSerializers(serializers.ModelSerializer):
    """Вывод постов без авторизации"""
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    count_reviews = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'author',
                  'create_at', 'author', 'count_reviews')
