from django.urls import path
from .views import ListPostView


urlpatterns = [
    path('list/', ListPostView.as_view()),


]
