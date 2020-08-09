from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import HasUserOrGroupPermission
from users.api.serializers import UsersSerializer, UserSerializer, RequestUserPermissionsSerializer, RequestUserAuthSerializer
from users.models import User


class UsersListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = [IsAdminUser, HasUserOrGroupPermission]
    required_permissions = {
        'GET': ['has_users_list']
    }


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, HasUserOrGroupPermission]
    required_permissions = {
        'GET': ['has_users_list']
    }


class RequestUserPermissionsRetrieveAPIView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = RequestUserPermissionsSerializer(request.user)
        return Response(serializer.data)


class RequestUserAuthRetrieveAPIView(generics.RetrieveAPIView):
    
    def get(self, request):
        serializer = RequestUserAuthSerializer(request.user)
        return Response(serializer.data)