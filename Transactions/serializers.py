from Store.models import Store
from rest_framework import serializers
from .models import Transaction
import ipdb

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type_transaction', 'date', 'hour', 'value', 'cpf', 'card', 'operation', 'store']
        