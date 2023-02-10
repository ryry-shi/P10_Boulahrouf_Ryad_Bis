from django.db import models
from user.models import MyUser


class Projects(models.Model):

    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(
        to=MyUser, on_delete=models.CASCADE, related_name="project_user_id"
    )


class Contributors(models.Model):


    role = models.CharField(
        max_length=50,
    )
    user_id = models.IntegerField()
    project_id = models.IntegerField()


class Issues(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    project_id = models.IntegerField()
    status = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(
        to=MyUser, on_delete=models.CASCADE, related_name="author_user"
    )
    assignee_user_id = models.ForeignKey(
        to=MyUser, on_delete=models.CASCADE, related_name="assigne_issue"
    )
    created_time = models.DateTimeField(auto_now=True)


# Create your models here.
