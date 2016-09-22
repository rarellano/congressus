# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-20 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0009_auto_20160721_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketwindowcashmovement',
            name='amount',
            field=models.FloatField(default=0, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='change',
            field=models.FloatField(default=0, verbose_name='change'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='payed',
            field=models.FloatField(default=0, verbose_name='payed'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='price',
            field=models.FloatField(default=0, verbose_name='price'),
        ),
    ]