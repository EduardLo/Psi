# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_clasif', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_test', models.CharField(max_length=150, unique=True)),
                ('clasif', models.ManyToManyField(blank=True, to='polls.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('cuest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.cuestionario')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.preguntas'),
        ),
    ]
