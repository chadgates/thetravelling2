# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_auto_20170210_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rsvp',
            options={'permissions': (('view_list', 'Can see the RSVP list'),)},
        ),
    ]