# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 22:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Instituciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instituciones',
            old_name='CoordenadaX',
            new_name='coordenadaX',
        ),
        migrations.RenameField(
            model_name='instituciones',
            old_name='CoordenadaY',
            new_name='coordenadaY',
        ),
        migrations.RenameField(
            model_name='instituciones',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='instituciones',
            old_name='InstitucionID',
            new_name='institucionID',
        ),
        migrations.RenameField(
            model_name='instituciones',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='instituciones',
            old_name='Telefono',
            new_name='telefono',
        ),
    ]
