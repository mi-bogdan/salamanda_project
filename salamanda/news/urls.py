from django.urls import path
from .views import ListPostView, TagsView


urlpatterns = [
    path('list/', ListPostView.as_view()),
    path('tags/', TagsView.as_view()),

]
