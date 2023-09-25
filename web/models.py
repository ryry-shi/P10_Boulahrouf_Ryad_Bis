from django.db import models
from user.models import MyUser
from datetime import datetime
from django.db.models.constraints import UniqueConstraint

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
    user_id = models.ForeignKey(
        to=MyUser, on_delete=models.CASCADE, related_name="user_contribiter"
    )
    project_id = models.ForeignKey(
        to=Projects, on_delete=models.CASCADE, related_name="project_contribiter"
    )
    
    class Meta:
           
        constraints = [UniqueConstraint(fields=['user_id'], name='unique_draft_user')
]


class Issue(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=10,choices=[("FAIBLE","FAIBLE"), ("MOYENNE","MOYENNE"),("ÉLEVÉE","ÉLEVÉE")])
    project_id = models.ForeignKey(
        to=Projects, on_delete=models.CASCADE, related_name="issue_user"
    )
    status = models.CharField(max_length=10,choices=[("À FAIRE","FAIBLE"), ("EN COURS","EN COURS"),("TERMINÉ","TERMINÉ")])
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
