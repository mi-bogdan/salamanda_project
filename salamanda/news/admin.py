from django.contrib import admin
from .models import Ip, Post, Tags, Review, Communities


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published',
                    'voting', 'create_at', 'update_at')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Ip)
class IpAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip')
    list_display_links = ('id', 'ip')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text', 'perents')
    list_display_links = ('id', 'user')


@admin.register(Communities)
class CommunitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',
                    'create_at', 'admin_communities')
    list_display_links = ('id', 'title')
