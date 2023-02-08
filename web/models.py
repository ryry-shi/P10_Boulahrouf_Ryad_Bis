from django.db import models
from user.models import MyUser


class Projects(models.Model):

    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    author = models.ForeignKey(
        to=MyUser,
        on_delete=models.CASCADE,
    )

# Create your models here.
