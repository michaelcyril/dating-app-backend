from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *



class ImageView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = ImagePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"save": True})
        return Response({"save": False, "errors": serializer.errors})

    @staticmethod
    def get(request):
        accountId = request.GET.get("accountId")
        print("id: "+accountId)
        try:
            # account = Account.objects.get(id=accountId)
          
            posts = Image.objects.filter(account_id=accountId)
            # posts = Image.objects.all()
            serializer = ImageGetSerializer(instance=posts, many=True)
            print("images")
            print(serializer.data)
            
                        
            return Response({"isAccountValid": True, "post": serializer.data})
        except Account.DoesNotExist:
            return Response({"isAccountValid": False})


class DeleteUpdateImagePost(APIView):
    @staticmethod
    def get(request):
        imageId = request.GET.get("imageId")
        try:
            post = Image.objects.get(id=imageId)
            post.delete()
            return Response({"delete": True})
        except Image.DoesNotExist:
            return Response({"delete": False})

    @staticmethod
    def post(request):
        pass



class VideoView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = VideoPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"save": True})
        return Response({"save": False, "errors": serializer.errors})

    @staticmethod
    def get(request):
        accountId = request.GET.get("accountId")
        try:
            # account = Account.objects.get(id=accountId)
            posts = Video.objects.filter(account_id=accountId)
            # posts = Video.objects.all()
            serializer = VideoGetSerializer(instance=posts, many=True)
            print("video")
            print(serializer.data)
            
            return Response({"isAccountValid": True, "post": serializer.data})
        except Account.DoesNotExist:
            return Response({"isAccountValid": False})


class DeleteUpdateVideoPost(APIView):
    @staticmethod
    def get(request):
        videoId = request.GET.get("videoId")
        try:
            post = Video.objects.get(id=videoId)
            post.delete()
            return Response({"delete": True})
        except Image.DoesNotExist:
            return Response({"delete": False})

    @staticmethod
    def post(request):
        pass

