# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0019_auto_20170726_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountinfo',
            old_name='company_logo_sqaure',
            new_name='company_logo_square',
        ),
    ]
