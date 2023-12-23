from django.urls import path
from .views import *
app_name = 'post_management'

urlpatterns = [
    path('create-get-image', ImageView.as_view()),
    path('create-get-video', VideoView.as_view()),
    path('delete-image', DeleteUpdateImagePost.as_view()),
    path('delete-video', DeleteUpdateVideoPost.as_view()),
]