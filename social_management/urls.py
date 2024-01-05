from django.urls import path
from .views import *
app_name = 'social_management'

urlpatterns = [
    path('like-user', LikeView.as_view()),
    path('conversation-view', ConversationView.as_view()),
    path('message-view', MessageView.as_view()),
]