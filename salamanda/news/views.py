from .serializers import PostListSerializers, TagsSerializers, PostDetailSerializers
from .models import Post, Ip, Tags, Review
from .service import add_str_tags

from accounts.models import Profile

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions


from django.db.models import Count
from django.contrib.auth.models import User
from django.db.models import Q


class ListPostView(APIView):
    """Получение постов авторизованых пользователей и не авторзованных пользователей """

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if token:
            user = User.objects.get(pk=request.user.id)
            profil = Profile.objects.get(user=user)
            array_key_word = profil.key_words.split(',')
            q_list = Q()

            for item in array_key_word:
                q_list |= Q(title__icontains=item)

            post = Post.objects.filter(q_list).annotate(
                count_reviews=Count('review'))

            serializers = PostListSerializers(post, many=True)

        else:
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

        profil = Profile.objects.get(user=user)
        profil.key_words += add_str_tags(request.data)
        profil.save()

        return Response(status=201)


class PostDetailView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializers = PostDetailSerializers(post)
        return Response(serializers.data)
