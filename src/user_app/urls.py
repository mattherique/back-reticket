from django.urls import path
from src.user_app.views import ListUsersView, SingleUserView, ListUsersByView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('users', ListUsersView.as_view(), name='list-users'),
    path('user', SingleUserView.as_view(), name='single-user'),
    path('users/by/', ListUsersByView.as_view(), name='single-user-with-id'),
    path('user/register', UserRegistrationView.as_view(), name='user-registration'),
    path('user/login', UserLoginView.as_view(), name='user-login'),
]