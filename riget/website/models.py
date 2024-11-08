from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class ZooUser(AbstractUser):
    phonenum = models.CharField(max_length=14, blank=True)
    points = models.IntegerField(default = 0)