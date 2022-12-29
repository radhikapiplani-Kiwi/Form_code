from django.db import models

# Create your models here.
from django.db import models

class employee(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    ispublic=models.CharField(max_length=1)
    ispublic == (
        ("Y", "yes"),
        ("N", "no"),
    )