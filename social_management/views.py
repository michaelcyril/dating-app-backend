from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from user_management.models import Account


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
