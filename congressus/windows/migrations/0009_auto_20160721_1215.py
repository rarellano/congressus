# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0008_ticketwindow_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketwindow',
            name='online',
            field=models.BooleanField(default=False, verbose_name='online'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
