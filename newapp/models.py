from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    notes = models.CharField(max_length=300)
    datetime = models.DateTimeField(default=datetime.now())