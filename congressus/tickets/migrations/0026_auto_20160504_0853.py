# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0025_auto_20160429_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=200, unique=True, verbose_name='Order')),
                ('order_tpv', models.CharField(blank=True, max_length=12, null=True, verbose_name='Order TPV')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('confirmed_date', models.DateTimeField(blank=True, null=True, verbose_name='Confirmed at')),
                ('confirmed', models.BooleanField(default=False)),
                ('confirm_sent', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('extra_data', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model, tickets.models.BaseTicketMixing),
        ),
        migrations.AddField(
            model_name='ticket',
            name='mp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.MultiPurchase'),
        ),
    ]