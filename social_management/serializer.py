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


class ConversationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            'initiator',
            'receiver'
        ]


class ConversationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        depth = 2


class MessagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'sender',
            'text',
            'conversation_id'
        ]


class MessageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        depth = 2