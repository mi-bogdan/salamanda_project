from django.shortcuts import render
from .serializers import PostListSerializers, TagsSerializers
from .models import Post, Ip, Tags, Review

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from django.db.models import Count
from django.contrib.auth.models import User


class ListPostView(APIView):

    def get(self, request):
        # token = request.META.get('HTTP_AUTHORIZATION')
        # if token:
        #     pass
        # else:
        post = Post.objects.filter(published=True).annotate(
            count_reviews=Count('review'))

        serializers = PostListSerializers(post, many=True)

        return Response(serializers.data)


class TagsView(APIView):
    """Теги. Добавление тегов к ключевым словам к пользователю"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tags = Tags.objects.all()
        serializers = TagsSerializers(tags, many=True)
        return Response(serializers.data)

    def post(self, request):
        """Добавление ключевых слов к пользоватклю, для поиска рекомендаций"""

        user = User.objects.get(pk=request.user.id)

        serializers = request.data
        key_word = []

        for item_dict in serializers:
            for key, value in item_dict.items():
                if key == 'title':
                    key_word.append(value)
        string = ','.join(key_word)
       

        
        return Response(status=201)
