# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20161103_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioperfil',
            name='ciudad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='usuarioperfil',
            name='pais',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
