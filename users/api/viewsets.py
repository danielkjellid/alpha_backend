from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import generics, permissions, status, filters
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination

from core.authentication import JWTAuthenticationSafe
from core.permissions import HasUserOrGroupPermission
from users.api.serializers import (PasswordResetConfirmSerializer,
                                   PasswordResetSerializer,
                                   RequestUserSerializer, UserCreateSerializer,
                                   UserSerializer, UsersSerializer)
from users.models import User
from utils.models import AuditLog

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)

class PageNumberSetPagination(PageNumberPagination):
    page_size = 18
    page_size_query_param = 'page_size'
    ordering = 'id'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'meta': {
                'current_page': int(self.request.query_params.get('page', 1)),
                'total': self.page.paginator.count,
                'current_range': '%s - %s' % (self.page.start_index(), self.page.end_index()),
                'total_pages': self.page.paginator.num_pages,
            },
            'results': data,
        })

class UsersListAPIView(generics.ListAPIView):
    """
    View for listing all users in the application
    """

    queryset = User.objects.all().order_by('id')
    serializer_class = UsersSerializer
    pagination_class = PageNumberSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    required_permissions = {
        'GET': ['has_users_list']
    }


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for viewing a single user instance
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, HasUserOrGroupPermission)
    required_permissions = {
        'GET': ['has_users_list']
    }

    def put(self, request, pk):
        user = get_object_or_404(User, pk = pk)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            old_user_instance = get_object_or_404(User, pk = pk)
            serializer.save()
            AuditLog.create_log_entry(request.user, User, old_user_instance)

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RequestUserRetrieveAPIView(generics.RetrieveAPIView):
    """
    View for getting info about request user
    """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthenticationSafe, )

    def get(self, request):
        serializer = RequestUserSerializer(request.user)
        return Response(serializer.data)


class UserCreateAPIView(generics.CreateAPIView):
    """
    View for creating a user instance
    """

    # set view public
    permission_classes = (AllowAny, )
    authentication_classes = ()

    # use the UserCreate serializer
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(generics.GenericAPIView):
    """
    View for reseting password.

    Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        """
        Create a serializer with request.data
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {'detail': _('Password reset e-mail has been sent.')},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmView(generics.GenericAPIView):
    """
    Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accept the following POST parameters: token, uid, new_password1, 
    new_password2

    Returns the success/fail message.
    """
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny, )
    authentication_classes = ()

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'detail': _('Password has been reset with the new password')})