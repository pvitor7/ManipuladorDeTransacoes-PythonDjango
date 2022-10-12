import uuid
from django.db import models

# Create your models here.
class Movement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    file = models.FileField()
    
