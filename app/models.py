from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    engine = models.CharField(max_length=40)