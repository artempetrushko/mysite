from django.db import models


class Registration(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
