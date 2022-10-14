from rest_framework import generics
from movements.models import Movement
from movements.serializers import MovementSerializer
from rest_framework.views import Response, status

class MovementsView(generics.CreateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    