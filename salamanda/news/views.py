from django.shortcuts import render
from .serializers import PostListSerializers
from .models import Post, Ip, Tags, Review

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from django.db.models import Count


class ListPostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # is_token = request.META.get('HTTP_AUTHORIZATION')
        # if is_token:
        #     pass
        # else:
        post = Post.objects.filter(published=True).annotate(
            count_reviews=Count('review'))

        serializers = PostListSerializers(post, many=True)
       
        return Response(serializers.data)
