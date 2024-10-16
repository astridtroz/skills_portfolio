# Generated by Django 5.1 on 2024-08-18 17:00

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userchat', '0013_alter_chatgroup_group_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='created',
            field=models.CharField(max_length=20),
        ),
    ]
