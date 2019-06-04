from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField

class User(models.Model):
    roll = models.CharField(max_length = 10, primary_key=True, unique=True)
    username = models.CharField(max_length = 10)
    name = models.CharField(max_length = 100)
    program=models.CharField(max_length = 20)
    dept = models.CharField(max_length = 50)
    hall = models.CharField(max_length = 15)
    room = models.CharField(max_length = 20)
    blood_group = models.CharField(max_length = 4)
    gender = models.CharField(max_length = 10)
    hometown = models.CharField(max_length = 100)
    fblink = models.URLField(max_length = 120)
    por = JSONField()
    earlier_login = models.BooleanField()
