# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('authentication', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(to='authentication.CustomUser'),
        ),
    ]
