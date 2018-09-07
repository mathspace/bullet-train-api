# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-17 16:46
from __future__ import unicode_literals

from django.db import migrations, models

try:
    from app import utils
except ModuleNotFoundError:
    from bullet_train_api.app import utils


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_identity_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='api_key',
            field=models.CharField(default=utils.create_hash, max_length=100, unique=True),
        ),
    ]
