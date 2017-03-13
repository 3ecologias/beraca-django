# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 19:01
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_merge_20170313_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceIcons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, upload_to=core.models.generate_filename, verbose_name='\xcdcone')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='T\xedtulo')),
            ],
        ),
        migrations.RemoveField(
            model_name='serviceitem',
            name='action_icon',
        ),
        migrations.RemoveField(
            model_name='serviceitem',
            name='action_title',
        ),
        migrations.RemoveField(
            model_name='serviceitem',
            name='disc_icon',
        ),
        migrations.RemoveField(
            model_name='serviceitem',
            name='disc_title',
        ),
        migrations.RemoveField(
            model_name='serviceitem',
            name='plan_icon',
        ),
        migrations.RemoveField(
            model_name='serviceitem',
            name='plan_title',
        ),
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
        migrations.AddField(
            model_name='serviceicons',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icones', to='core.ServiceItem'),
        ),
    ]