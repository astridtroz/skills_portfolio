# Generated by Django 5.1 on 2024-08-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0008_alter_assignment_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
