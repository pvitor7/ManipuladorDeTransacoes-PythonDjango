import uuid
from django.db import models

    
class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type_transaction = models.IntegerField()
    date = models.DateField()
    hour = models.TimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=128)
    card = models.CharField(max_length=128)
    store = models.ForeignKey('Store.Store', on_delete=models.CASCADE, related_name='transaction')
