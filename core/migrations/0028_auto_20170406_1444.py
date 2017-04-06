# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 17:44
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20170406_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimages',
            name='image',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(verbose_name='Corpo do texto'),
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
        migrations.AlterField(
            model_name='serviceitem',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descri\xe7\xe3o'),
        ),
    ]