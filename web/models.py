from django.db import models
from user.models import MyUser
from datetime import datetime


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    project_id = models.IntegerField(primary_key=True)
    author_user_id = models.ForeignKey(
        to=MyUser, on_delete=models.CASCADE, related_name="project_user_id"
    )


class Contributors(models.Model):
    role = models.CharField(
        max_length=128,
    )
    user_id = models.IntegerField()
    project_id = models.IntegerField()


class Issue(models.Model):
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


class Comment(models.Model):
    description = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(
        to=MyUser, on_delete=models.CASCADE, related_name="comment_author"
    )
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name="comment_issue")
    created_time = models.DateTimeField(auto_now=True)
