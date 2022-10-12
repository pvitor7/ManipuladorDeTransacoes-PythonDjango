from django import views
from .models import Account
from .serializers import AccountSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.views import Request, Response
from rest_framework import generics
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token


class AccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
class LoginView(views.ObtainAuthToken):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login_user = authenticate(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=login_user)
        return Response({"token": token.key})