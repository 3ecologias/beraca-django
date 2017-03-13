# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 19:20
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20170313_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=core.models.generate_filename, verbose_name='\xcdcone')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='T\xedtulo')),
                ('desc', models.TextField(blank=True, max_length=200, verbose_name='T\xedtulo')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='method', to='core.ServiceItem')),
            ],
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