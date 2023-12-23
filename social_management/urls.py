from django.urls import path
from .views import *
app_name = 'social_management'

urlpatterns = [
    path('like-user', LikeView.as_view()),
]