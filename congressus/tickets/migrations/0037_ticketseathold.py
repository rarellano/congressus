# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20160526_1115'),
        ('tickets', '0036_auto_20160523_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketSeatHold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=20)),
                ('seat', models.CharField(help_text='row-col', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.SeatLayout')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_holds', to='events.Session')),
            ],
        ),
    ]
