from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.all_users.users.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    """
        post:Create a new user.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
         put: update user
        patch: partial update user
        delete: delete user
    """

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return get_user_model().objects.filter(id=self.request.user.id)


