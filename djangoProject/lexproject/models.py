from django.db import models
class Modellex(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
