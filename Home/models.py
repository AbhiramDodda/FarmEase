from django.db import models

class HelloModel(models.Model):
    origin = models.CharField(max_length = 10)
