import json

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from user_management.models import Account, User
from django.db.models import Q
from .channel_manager import PostToChatChannel


class LikeView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = LikePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"like": True})
        return Response({"like": False})


    @staticmethod
    def get(request):
        accountId = request.GET.get("accountId")
        try:
            account = Account.objects.get(id=accountId)
            queryset = Like.objects.filter(account=account)
            serializer = LikeGetSerializer(instance=queryset, many=True)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return Response([])


class ConversationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        print(data)
        user1 = User.objects.get(id=data['initiator'])
        user2 = User.objects.get(id=data['receiver'])
        conversation = Conversation.objects.filter((Q(initiator=user1) & Q(receiver=user2)) | (Q(initiator=user2) & Q(receiver=user1)))
        if len(conversation)>=1:
            return Response({"save": False, "conv_id": conversation[0].id})
        serialized = ConversationPostSerializer(data=data)
        if serialized.is_valid():
            returned_data = serialized.save()
            return Response({"save": True, "conv_id": returned_data.id})

    @staticmethod
    def get(request):
        try:
            user = User.objects.get(id=request.GET.get('user_id'))
            queryset = Conversation.objects.filter(Q(receiver=user) | Q(initiator=user))
            serialized = ConversationGetSerializer(instance=queryset, many=True)
            print("DDDDDDD")
            print(serialized.data)
            return Response(serialized.data)
        except:
            return Response([])

class MessageView(APIView):
    @staticmethod
    def post(request):
        serialized = MessagePostSerializer(data=request.data)
        if serialized.is_valid():
            data = serialized.save()
            print("TTTTTTTTTTTTTTTT")
            toSocket = {
                "id": data.id,
                "sender": data.sender.id,
                'text': data.text,
                'conversation_id': data.conversation_id.id,
                'timestamp': data.timestamp
            }
            print(toSocket)
            toSocket['id'] = str(toSocket['id'])
            toSocket['sender'] = str(toSocket['sender'])
            toSocket['conversation_id'] = str(toSocket['conversation_id'])
            toSocket['timestamp'] = toSocket['timestamp'].isoformat()
            PostToChatChannel(toSocket)
            # print(toSocket['text'])
            return Response({"send": True,
                             "message": toSocket['text'],
                             })
          
        return Response({"send": False})

    @staticmethod
    def get(request):
        conv_id = request.GET.get("conv_id")
        try:
            conv = Conversation.objects.get(id=conv_id)
            queryset = Message.objects.values('id', 'sender', 'text', 'conversation_id', 'timestamp').filter(conversation_id=conv).order_by('-timestamp')[:20]
            # for msg in queryset:
            #    print(msg['text'])
            # serialized = MessageGetSerializer(instance=queryset, many=True)
            print("response")
            
            print(Response(queryset))
            return Response(queryset)
        except:
            return Response([])



# {
#     "sender": "hhhhhhhhhhhh",
#     "text": "Hello World ",
#     "conversation_id": "hhhhhhhhhhhh"
# }
