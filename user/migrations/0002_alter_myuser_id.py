# Generated by Django 4.1.6 on 2023-02-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]