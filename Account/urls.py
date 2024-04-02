from django.urls import path
from .views import Home, UserList, LogoutUser

urlpatterns = [
    path("", Home, name="home"),
    path("users/", UserList.as_view(), name="user-list"),
    path("logout/", LogoutUser.as_view(), name="logout"),
]


