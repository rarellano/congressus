# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-25 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0035_session_thermal_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='unit',
            field=models.BooleanField(default=True, verbose_name='per unit'),
        ),
    ]
