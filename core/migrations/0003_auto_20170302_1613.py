# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170302_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_item',
            name='lat',
            field=models.CharField(blank=True, max_length=100, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='portfolio_item',
            name='lon',
            field=models.CharField(blank=True, max_length=100, verbose_name='Longitude'),
        ),
    ]
