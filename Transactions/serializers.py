from rest_framework import serializers

from Store.serializers import StoreSerializer
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type_transaction', 'date', 'hour', 'value', 'cpf', 'card', 'store']

    