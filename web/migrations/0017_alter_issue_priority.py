# Generated by Django 4.1.6 on 2023-06-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_issue_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[(1, '1'), (2, '2')], max_length=10),
        ),
    ]
