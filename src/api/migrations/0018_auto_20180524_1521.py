# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

try:
    from users import apps
    _dependencies = [
        ('users', '0013_auto_20180524_1521'),
        ('api', '0017_feature_description'),
    ]
except ModuleNotFoundError:
    _dependencies = [
        ('api', '0017_feature_description'),
    ]


class Migration(migrations.Migration):

    dependencies = _dependencies

    operations = [
        migrations.AlterField(
            model_name='project',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='organisations.Organisation'),
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
    ]
