from django.urls import path
from .views import Home, UserList, LogoutUser, UserDetail

urlpatterns = [
    path("", Home, name="home"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<str:pk>/", UserDetail.as_view(), name="user-data"),
    path("logout/", LogoutUser.as_view(), name="logout"),
]


