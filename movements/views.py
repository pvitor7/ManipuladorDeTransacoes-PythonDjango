from rest_framework import generics
from accounts.permissions import UserPermission
from movements.models import Movement
from movements.serializers import MovementSerializer
import ipdb; 

class MovementsView(generics.CreateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    # def perform_create(self, serializer):
        # ipdb.set_trace()
        # self.request.data['user'] = self.request.user
        # print(self.request.user)
        # serializer.save(user=self.request.user)