from django.db import models

class Event(models.Model):
    date = models.CharField(max_length=254)
    tournament = models.CharField(max_length=254)
    match = models.CharField(max_length=254)
    hour = models.CharField(max_length=60)
    tv = models.CharField(max_length=60)
