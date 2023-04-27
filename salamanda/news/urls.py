from django.urls import path
from .views import ListPostView, TagsView, PostDetailView


urlpatterns = [
    path('list/', ListPostView.as_view()),
    path('tags/', TagsView.as_view()),
    path('post/<pk>/', PostDetailView.as_view()),


]
