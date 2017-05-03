# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_interpretacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('email', models.CharField(max_length=100, verbose_name='Correo')),
            ],
        ),
        migrations.CreateModel(
            name='resultadoGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.IntegerField(default=0)),
                ('dateTest', models.DateTimeField(verbose_name='date resuelto')),
                ('testRealizado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.cuestionario')),
                ('usuario', models.ForeignKey(default='Invitado', on_delete=django.db.models.deletion.CASCADE, to='polls.Invitado')),
            ],
        ),
    ]