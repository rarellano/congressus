# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-09 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0030_auto_20160831_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettemplate',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='note'),
        ),
    ]
