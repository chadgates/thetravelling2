# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170210_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, verbose_name='ZIP Code'),
        ),
    ]
