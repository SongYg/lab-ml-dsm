# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-12 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='module_name',
            field=models.CharField(default='-1', max_length=100),
        ),
    ]
