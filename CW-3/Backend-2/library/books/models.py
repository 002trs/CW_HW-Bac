from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя")
    surname = models.CharField(max_length=12, verbose_name="Фамилия")
    year = models.IntegerField(null=True, verbose_name="Возраст")
    country = models.CharField(max_length=128, verbose_name="Страна")
    dirthdate = models.DateField(null=True, verbose_name="День рождения")


