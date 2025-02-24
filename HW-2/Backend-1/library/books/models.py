from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=128)
    year = models.DateField(null=True)
    city = models.CharField(max_length=128)
