# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SSInstituciones',
            fields=[
                ('institucionID', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('coordenadaX', models.FloatField(null=True)),
                ('coordenadaY', models.FloatField(null=True)),
            ],
        ),
    ]
