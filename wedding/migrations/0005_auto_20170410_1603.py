# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-10 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_auto_20170407_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='amount',
            new_name='quantity',
        ),
    ]
