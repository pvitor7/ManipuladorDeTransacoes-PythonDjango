from rest_framework import generics
from movements.models import Movement
from movements.serializers import MovementSerializer


class MovementsView(generics.ListCreateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
