# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-10 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0005_auto_20170410_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='buyer',
            new_name='user',
        ),
    ]
