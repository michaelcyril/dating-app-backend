from rest_framework import serializers
from .models import *


class ImagePostSerializer(serializers.ModelSerializer):
    binary_data = serializers.FileField(required=False)
    class Meta:
        model = Image
        fields = [
            'account',
            'image',
            'binary_data',
        ]

    def create(self, validated_data):
        binary_data = validated_data.pop('binary_data', None)
        instance = super().create(validated_data)

        if binary_data:
            instance.binary_data = binary_data.read()
            instance.save()

        return instance


class ImageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        depth = 1


class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'account',
            'thumbnail',
            'video',
        ]


class VideoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        depth = 1