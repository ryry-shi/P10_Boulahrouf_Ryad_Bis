# Generated by Django 4.1.6 on 2023-03-09 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contributors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.CharField(max_length=128)),
                ("author_user_id", models.IntegerField()),
                ("project_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
            fields=[
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("project_id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "author_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("desc", models.CharField(max_length=50)),
                ("tag", models.CharField(max_length=50)),
                ("priority", models.CharField(max_length=50)),
                ("project_id", models.IntegerField()),
                ("status", models.CharField(max_length=50)),
                ("created_time", models.DateTimeField(auto_now=True)),
                (
                    "assignee_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigne_issue",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=50)),
                ("created_time", models.DateTimeField(auto_now=True)),
                (
                    "author_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "issue_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_issue",
                        to="web.issue",
                    ),
                ),
            ],
        ),
    ]
