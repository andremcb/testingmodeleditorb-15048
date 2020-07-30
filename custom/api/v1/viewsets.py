from rest_framework import authentication
from custom.models import UserLogin
from .serializers import UserLoginSerializer
from rest_framework import viewsets


class UserLoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserLoginSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UserLogin.objects.all()
