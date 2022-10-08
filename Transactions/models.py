import uuid
from django.db import models

from Store.models import Store
    
class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type_transaction = models.IntegerField()
    date = models.CharField(max_length=128)
    hour = models.CharField(max_length=128)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    cpf = models.CharField(max_length=128)
    card = models.CharField(max_length=128)
    
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
