from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):

    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["username"], name="unique user")]


# Create your models here.
