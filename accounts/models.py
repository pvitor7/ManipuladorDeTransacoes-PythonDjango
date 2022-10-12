import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=48, unique=True)
    password = models.CharField(max_length=48)
    
