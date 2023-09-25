# Generated by Django 4.1.6 on 2023-06-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('À FAIRE', 'FAIBLE'), ('EN COURS', 'EN COURS'), ('TERMINÉ', 'TERMINÉ')], max_length=10),
        ),
    ]
