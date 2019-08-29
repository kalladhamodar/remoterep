# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-14 06:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdata',
            old_name='productclass',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='productcolor',
            new_name='Constituecy',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='productname',
            new_name='District',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='productcost',
            new_name='State',
        ),
        migrations.RemoveField(
            model_name='productdata',
            name='productid',
        ),
        migrations.AddField(
            model_name='productdata',
            name='mobile',
            field=models.BigIntegerField(default=datetime.datetime(2019, 7, 14, 6, 15, 46, 624984, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdata',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 7, 14, 6, 16, 4, 509314, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
