# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 15:38
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170307_1229'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='serviceitem',
            name='action_icon',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='\xcdcone A\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='dev_img',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='Imagem de Desenvolvimento'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='disc_icon',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='\xcdcone Discuss\xe3o'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='icon',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='\xcdcone'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='method_img',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='Imagem da Metodologia'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='plan_icon',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='\xcdcone Planejamento'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='sustainable_img',
            field=models.ImageField(upload_to=core.models.generate_filename, verbose_name='Imagem de Sustentabilidade'),
        ),
    ]