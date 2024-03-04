from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.forms import PasswordChangeForm
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'gender',
            'email',
            'phone',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class AccountPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'user',
            'location',
            'work',
            'profile',
            'bio',
            'tags',
        ]


class AccountGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        depth = 2


#   For tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class AccountTagUpdateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)  # Nested serializer for tags

    class Meta:
        model = Account
        fields = ['id', 'tags']

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.tags.clear()
        print(len(tags_data))
        for tag_data in tags_data:
            print("Tag Data:", tag_data)
            tag_name = tag_data.get('name')
            if tag_name:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
            else:
                print("Error: Tag name not found in tag data")
        return instance
        # tags_data = validated_data.pop('tags', [])
        # instance.tags.clear()  # Clear existing tags
        # for tag_data in tags_data:
        #     tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
        #     instance.tags.add(tag)
        # return instance
