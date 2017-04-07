# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-07 20:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wedding', '0003_auto_20170214_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField(verbose_name='Item count')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('link', models.TextField(blank=True, null=True, verbose_name='Link')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
                ('gift_is_part', models.BooleanField(default=False, verbose_name='Gift is part')),
                ('max_parts', models.PositiveIntegerField(verbose_name='Maximum number of parts')),
                ('taken_parts', models.PositiveIntegerField(default=0, verbose_name='Number of parts taken')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Gift',
                'verbose_name_plural': 'Gifts',
            },
        ),
        migrations.CreateModel(
            name='GiftOrder',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('voucher_from', models.CharField(max_length=300, verbose_name='Voucher is from')),
                ('voucher_greeting', models.TextField(blank=True, null=True, verbose_name='Voucher Greeting')),
                ('voucher_senddirect', models.BooleanField(default=False, verbose_name='Send voucher directly')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GiftOrderItem',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(verbose_name='Item count')),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.Gift')),
                ('giftorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.GiftOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='rsvp',
            options={'permissions': (('view_list', 'Can see the RSVP list'),), 'verbose_name': 'RSVP', 'verbose_name_plural': 'RSVPs'},
        ),
        migrations.AddField(
            model_name='cartitem',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.Gift'),
        ),
    ]
