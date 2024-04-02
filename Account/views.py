from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.http import HttpResponse

from .permissions import IsPublicProfileOrAdmin
from .models import User
from .serializers import UserSerializer

def Home(request):
    return HttpResponse("Hello World")


class UserList(APIView):
    permission_classes = [IsPublicProfileOrAdmin, IsAuthenticated]

    def get(self, request):
        print(self.request.user)
        if self.request.user.is_superuser:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        queryset = User.objects.filter(is_public=True)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# Logout the user
class LogoutUser(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response("User Logout Successfully",status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)