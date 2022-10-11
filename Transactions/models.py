from random import choices
from unittest.mock import DEFAULT
import uuid
from django.db import models


class OperationsOptions(models.TextChoices):
    entry = 'Entrada'
    out = 'Saída'
    
class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type_transaction = models.IntegerField()
    date = models.DateField()
    hour = models.TimeField()
    value = models.CharField(max_length=20)
    cpf = models.CharField(max_length=128)
    card = models.CharField(max_length=128)
    store = models.ForeignKey('Store.Store', on_delete=models.CASCADE, related_name='transaction')
    operation = models.CharField(max_length=10, choices=OperationsOptions.choices, default=None, blank=True, null=True)
