# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 17:04
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170303_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='sub_title',
            field=models.CharField(max_length=20, null=True, verbose_name='Sub-t\xedtulo'),
        ),
        migrations.AlterField(
            model_name='portfolioimages',
            name='image',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='Primeira imagem(slide)'),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='miniature',
            field=models.ImageField(upload_to=core.models.generate_filename_miniature, verbose_name='Miniatura'),
        ),
    ]
