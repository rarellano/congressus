# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 09:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0037_ticketseathold'),
        ('windows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketWindowSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('payed', models.PositiveIntegerField(default=0)),
                ('change', models.PositiveIntegerField(default=0)),
                ('payment', models.CharField(choices=[('cash', 'Cash'), ('card', 'Credit Card')], default='cash', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='tickets.MultiPurchase')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='ticketwindow',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ticketwindow',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='windows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticketwindowsale',
            name='window',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='windows.TicketWindow'),
        ),
    ]
