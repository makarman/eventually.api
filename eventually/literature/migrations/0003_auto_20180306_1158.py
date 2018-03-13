# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-06 09:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0002_foreign_key_to_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literatureitem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]