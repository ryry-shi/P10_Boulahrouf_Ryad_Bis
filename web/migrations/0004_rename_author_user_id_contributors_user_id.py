# Generated by Django 4.1.6 on 2023-03-17 20:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_rename_issue_id_comment_issue"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contributors",
            old_name="author_user_id",
            new_name="user_id",
        ),
    ]