from django.urls import path
from .views import *
app_name = 'user_management'

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login', LoginView.as_view()),
    path('user-information<slug:query_type>', UserInformation.as_view()),
    # path('change-password', ChangePasswordView.as_view()),
    path('change-password', change_password),
    path('update-user', UpdateUserView.as_view()),
    path('get-create-account/<slug:userId>', AccountView.as_view()),
    path('delete-update-account', DeleteUpdateAccount.as_view()),
    path('update-dob-account', UpdateDBO.as_view()),
    path('change-user-status', ChangeUserStatus.as_view()),
    path('all-account/<slug:accountId>', AllAccountView.as_view()),

    path('check-network', CheckNetwork.as_view()),
    path('update-lat-long', UpdateLatLongView.as_view()),
    path('delete-user-account', DeleteUser.as_view()),
    # path('delete-update-bin', TrashBinView.as_view()),
]
