# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20160124_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='vericode',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
