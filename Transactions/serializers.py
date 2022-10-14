from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type_transaction', 'date', 'hour', 'value', 'cpf', 'card', 'operation', 'store']
        