# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0024_auto_20160429_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tshirt',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='TShirt',
        ),
    ]
