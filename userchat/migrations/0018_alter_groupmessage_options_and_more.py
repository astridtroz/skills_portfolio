# Generated by Django 5.1 on 2024-08-18 18:02

import django.utils.timezone
import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userchat', '0017_alter_chatgroup_group_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupmessage',
            options={},
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='created',
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
    ]
