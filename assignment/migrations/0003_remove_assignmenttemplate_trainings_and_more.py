# Generated by Django 5.0.7 on 2024-08-15 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_rename_training_assignmenttemplate_trainings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmenttemplate',
            name='trainings',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='AssignmentTemplate',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
    ]
