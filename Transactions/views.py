import locale
from rest_framework import generics
from rest_framework.views import Response
from .models import Transaction
from .serializers import TransactionSerializer
from django.forms import model_to_dict

class TransactionsView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        total = 0
        transactions = []
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        
        for item in self.queryset.all():
            
            value_formated = item.value[:-2].replace(',', '')
            value_formated = value_formated.replace('.', '')
            
            if item.operation == 'Entrada':
                total = total - int(value_formated)
                item.value = locale.currency(int(value_formated), grouping=True, symbol="BRL")
            else:
                total += int(value_formated)
                item.value = locale.currency(int(f'-{value_formated}'), grouping=True, symbol="BRL")
                
            transactions.append(model_to_dict(item))
            
            
        total_money = locale.currency(int(total), grouping=True, symbol="BRL")
        return Response([{'total': total_money}, transactions])