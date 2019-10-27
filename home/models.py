from django.db import models

# Create your models here.
class accounts(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=150)
    secret = models.CharField(max_length=150)