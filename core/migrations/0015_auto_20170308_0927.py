# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 12:27
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170308_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='anchor',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='\xc2ncora/Tab'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogimages',
            name='image',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='Imagem'),
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
