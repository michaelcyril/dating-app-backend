from rest_framework import serializers
from .models import *


class ImagePostSerializer(serializers.ModelSerializer):
    # binary_data = serializers.FileField(required=False)
    # binary_data = serializers.CharField(required=False)
    
    class Meta:
        model = Image
        fields = [
            'account',
            'image',
            'binary_data',
        ]

    def create(self, validated_data):
        binary_data = validated_data.pop('binary_data', None)
        print("before decode")
        print(binary_data)
        
        
        instance = super().create(validated_data)

        if binary_data:
            instance.binary_data = binary_data
            instance.save()
            print(instance)
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
            'binary_data'
        ]
        
    def create(self, validated_data):
        binary_data = validated_data.pop('binary_data', None)
        print("before decode")
        print(binary_data)
        
        
        instance = super().create(validated_data)

        if binary_data:
            instance.binary_data = binary_data
            instance.save()
            print(instance)
        return instance


class VideoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        depth = 1