from django.urls import path
from src.user_app.views import ListUsersView, SingleUserView, ListUsersByView

urlpatterns = [
    path('users', ListUsersView.as_view(), name='list-users'),
    path('user', SingleUserView.as_view(), name='single-user'),
    path('users/by/', ListUsersByView.as_view(), name='single-user-with-id'),
]