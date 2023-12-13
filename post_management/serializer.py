from rest_framework import serializers
from .models import *


class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'account',
            'image',
        ]


class ImageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        depth = 2


class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'account',
            'video',
        ]


class VideoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        depth = 2