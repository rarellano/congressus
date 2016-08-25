# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0048_ticket_used_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationGenerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='amount')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='order')),
                ('concept', models.CharField(max_length=200, verbose_name='concept')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.InvitationType', verbose_name='type')),
            ],
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='type',
        ),
        migrations.AddField(
            model_name='invitation',
            name='generator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='tickets.InvitationGenerator', verbose_name='generator'),
        ),
    ]