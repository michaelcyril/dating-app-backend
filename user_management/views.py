from django.db.models import QuerySet
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .models import *
from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        print(request.data)
        serializer = UserSerializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            email = data['email']
            user = User.objects.filter(email=email)
            if user:
                message = {'status': False, 'message': 'username or email already exists'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            userr = serializer.save()
            acc = Account.objects.create(
                user = userr,
                location = "",
                work = "",
                bio = "Hey there i am using heartsync."
            )
            serialized = AccountPostSerializer(data=data)
            if serialized.is_valid():
                serialized.save()
            message = {'save': True}
            return Response(message)
        message = {'save': False, 'errors': serializer.errors}
        print(message)
        return Response(message)

    @staticmethod
    def get(request):
        users  = User.objects.all()
        return Response(UserSerializer(instance=users, many=True).data)
# {
# "email":"mike@gmail.com",
# "password":"123",
# "username":"mike",
# "phone":"078676726"
# }


class LoginView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')
        print('Data: ', email, password)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            user_id = User.objects.get(email=email)
            user_info = UserSerializer(instance=user_id, many=False).data
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'login': True,
                'token': token.key,
                'user': user_info
            }

            return Response(response)
        else:
            response = {
                'login': False,
                'msg': 'Invalid username or password',
            }

            return Response(response)

# {
# "email":"mike@gmail.com",
#     "password":"123"
# }


class UserInformation(APIView):

    @staticmethod
    def get(request, query_type):
        if query_type == 'single':
            try:
                user_id = request.GET.get('user_id')
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({'message': 'User Does Not Exist'})
            return Response(UserSerializer(instance=user, many=False).data)

        elif query_type == 'all':
            queryset = User.objects.all()
            return Response(UserSerializer(instance=queryset, many=True).data)

        else:
            return Response({'message': 'Wrong Request!'})


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        username = request.data['username']
        email = request.data['email']
        phone = request.data['phone']
        if phone_number:
            try:
                query = User.objects.get(email=email)
                query.email = email
                query.username = username
                query.phone = phone
                query.save()
                return Response({'save': True, "user": UserSerializer(instance=query, many=False).data})
            except User.DoesNotExist:
                return Response({'message': 'You can not change the email'})

        else:

            return Response({'message': 'Not Authorized to Update This User'})

class AllAccountView(APIView):
    @staticmethod
    def get(request, accountId):
        # userId = "9f57a7ab-3cf6-4086-95d5-fa987b9bbf14"
        queryset = Account.objects.all().exclude(id=accountId)
        serialized = AccountGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class AccountView(APIView):
    @staticmethod
    def get(request, userId):
        try:
            user = User.objects.get(id=userId)
            accounts = Account.objects.filter(user=user)
            if len(accounts) == 1:
                returned_data = Account.objects.get(user=user)
                serialized = AccountGetSerializer(instance=returned_data, many=False)
                return Response({"status": True, "data": serialized.data})
            else:
                data = {
                    "user": user.id,
                    "bio": "Hey there i am using heartsync.",
                    "work": "",
                    "location": ""
                }
                serialized = AccountPostSerializer(data=data)
                if serialized.is_valid():
                    serialized.save()
                    return Response({"status": False})
                else:
                    print(serialized.errors)
                    return Response({"status": False})
        except User.DoesNotExist:
            return Response({"status": False})



class DeleteUpdateAccount(APIView):
    @staticmethod
    def post(request):
        data = request.POST
        try:
            print(data['id'])
            account = Account.objects.get(id = data['id'])
            account.location = data['location']
            account.work  = data['work']
            if 'profile' in request.FILES:
                account.profile = request.FILES.get('profile')
            # account.dob = data['dob']
            account.bio = data['bio']
            account.save()
            return Response({"update": True})
        except Account.DoesNotExist:
            return Response({"update": False})

    @staticmethod
    def get(request):
        accountId = request.GET.get("accountId")
        try:
            account = Account.objects.get(id=accountId)
            account.delete()
            return Response({"delete": True})
        except Account.DoesNotExist:
            return Response({"delete": False})



# {
#     "id": "SSSSLLLSLSLL",
#     "location": "Kimara",
#     "work": "Fundi",
#     "profile": "Fundi",
#     "dob": "21-12-23",
#     "bio": "ddd"
# }


class ChangeUserStatus(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            user = User.objects.get(id=data['userId'])
            user.status = data['status_to']
            user.save()
            return Response({"change": True})
        except:
            return Response({"change": False})



# {
#     "userId": "hhhhhhhhh",
#     "status_to": "ACTIVE"
# }



