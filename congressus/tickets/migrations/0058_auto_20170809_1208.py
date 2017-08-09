# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0057_auto_20160916_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='multipurchase',
            name='payment_method',
            field=models.CharField(choices=[('tpv', 'TPV'), ('paypal', 'Paypal'), ('stripe', 'Stripe'), ('twcash', 'Cash, Ticket Window'), ('tpvcash', 'TPV, Ticket Window')], default='tpv', max_length=10, verbose_name='payment method'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(choices=[('tpv', 'TPV'), ('paypal', 'Paypal'), ('stripe', 'Stripe'), ('twcash', 'Cash, Ticket Window'), ('tpvcash', 'TPV, Ticket Window')], default='tpv', max_length=10, verbose_name='payment method'),
        ),
    ]
