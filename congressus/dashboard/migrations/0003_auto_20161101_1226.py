# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-01 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_dashboard_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configchart',
            name='type',
            field=models.CharField(choices=[('os_c', 'Online sales chart'), ('ws_c', 'Window sales chart'), ('a_c', 'Access chart'), ('os_p', 'Online sales pie'), ('ws_p', 'Window sales pie'), ('a_p', 'Access pie'), ('ws_b', 'Window sales bar')], default='os_c', max_length=8, verbose_name='type'),
        ),
    ]
