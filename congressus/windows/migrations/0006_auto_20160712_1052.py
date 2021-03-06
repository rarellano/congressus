# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0005_auto_20160617_0809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketwindow',
            options={'verbose_name': 'ticket window', 'verbose_name_plural': 'ticket windows'},
        ),
        migrations.AlterModelOptions(
            name='ticketwindowcashmovement',
            options={'verbose_name': 'ticket window cash movement', 'verbose_name_plural': 'ticket window cash movements'},
        ),
        migrations.AlterModelOptions(
            name='ticketwindowsale',
            options={'verbose_name': 'ticket window sale', 'verbose_name_plural': 'ticket window sales'},
        ),
        migrations.AlterField(
            model_name='ticketwindow',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='ticketwindowcashmovement',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='ticketwindowcashmovement',
            name='type',
            field=models.CharField(choices=[('add', 'Add'), ('remove', 'Remove')], default='add', max_length=10, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='change',
            field=models.PositiveIntegerField(default=0, verbose_name='change'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='payed',
            field=models.PositiveIntegerField(default=0, verbose_name='payed'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='payment',
            field=models.CharField(choices=[('cash', 'Cash'), ('card', 'Credit Card')], default='cash', max_length=10, verbose_name='payment'),
        ),
        migrations.AlterField(
            model_name='ticketwindowsale',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='price'),
        ),
    ]
