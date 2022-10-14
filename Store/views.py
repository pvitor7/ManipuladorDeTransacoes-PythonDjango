from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import UserPermission
from .models import Store
from .serializers import StoreSerializer


class StoresView(generics.ListAPIView):
    permission_classes = [UserPermission]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

