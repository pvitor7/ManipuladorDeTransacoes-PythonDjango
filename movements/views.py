from rest_framework import generics
from accounts.permissions import UserPermission
from movements.models import Movement
from movements.serializers import MovementSerializer
from django.forms import model_to_dict
import ipdb; 

class MovementsView(generics.CreateAPIView):
    permission_classes = [UserPermission]
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

