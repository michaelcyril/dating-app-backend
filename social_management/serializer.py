from rest_framework import serializers
from .models import *


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'account',
            'likedBy',
        ]


class LikeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        depth = 2
