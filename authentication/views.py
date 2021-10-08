from rest_framework import status

from rest_framework.permissions import AllowAny

from rest_framework.response import Response

from rest_framework import viewsets

from authentication.serializers import (LoginSerializer, RegistrationSerializer,)


class RegistrationView(viewsets.ViewSet):
    """
    Registration endpoint
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def create(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(viewsets.ViewSet):
    """
    Login endpoint
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
