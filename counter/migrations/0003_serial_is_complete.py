# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_serial_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]