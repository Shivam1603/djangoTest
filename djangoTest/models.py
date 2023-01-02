from django.db import models

class Security(models.Model):
    name = models.CharField(max_length = 100)
    isin = models.CharField(max_length = 11)