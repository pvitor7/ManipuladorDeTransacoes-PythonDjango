from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import Request, Response, status
from .models import Store
from .serializers import StoreSerializer
from Transactions.models import Transaction
import ipdb;

class StoresView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    
    def get(self, request: Request, *args, **kwargs) -> Response:
        import ipdb;
        stores_list = Store.objects.all()
        list_relations = [];
        
        for store in stores_list:
            list_transactions = [];
            transactions = Transaction.objects.filter(store=store.id)
            object_return = model_to_dict(store)
                
            for tran in transactions:
                list_transactions.append(model_to_dict(tran))
                    
            object_return['transactions'] = list_transactions
            list_relations.append(object_return)
        
        return Response({"Stores": list_relations}, status.HTTP_200_OK);
