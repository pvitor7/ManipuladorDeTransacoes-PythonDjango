from email.policy import default
from django.db import models

# Create your models here.
class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    store = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    
