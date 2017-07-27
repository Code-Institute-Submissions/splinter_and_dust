# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0018_auto_20170726_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfo',
            name='company_blurb',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='accountinfo',
            name='company_logo_sqaure',
            field=models.ImageField(null=True, upload_to='images/logo_sqaure'),
        ),
    ]
