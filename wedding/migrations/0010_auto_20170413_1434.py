# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-13 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0009_auto_20170413_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftorderitem',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giftitems', to='wedding.Gift'),
        ),
    ]
