from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profiles/', default='default.png')

    def __str__(self):
        return self.username
