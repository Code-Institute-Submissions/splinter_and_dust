# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0024_auto_20170727_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
