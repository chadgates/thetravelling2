# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170209_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('view_list', 'Can see the user list'),)},
        ),
    ]
