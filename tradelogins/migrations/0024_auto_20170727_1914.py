# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0023_auto_20170727_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('T', 'Trade'), ('C', 'Customer')], default=' ', max_length=2),
        ),
    ]
