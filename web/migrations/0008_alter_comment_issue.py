# Generated by Django 4.1.6 on 2023-04-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0007_alter_contributors_project_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="issue",
            field=models.IntegerField(),
        ),
    ]
