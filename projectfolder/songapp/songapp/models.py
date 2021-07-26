from django.db import models

class Artist (models.Model):
    name = models.CharField(max_length = 250)
    country = models.CharField(max_length = 150)
    birth_year = models.IntegerField()
    genre = models.CharField(max_length = 150)