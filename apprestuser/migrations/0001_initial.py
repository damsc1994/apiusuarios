# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.TextField(max_length='20')),
                ('apellidos', models.TextField(max_length='20')),
                ('edad', models.IntegerField()),
                ('direccion', models.TextField(max_length='100')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.TextField(max_length='10')),
                ('correo', models.TextField(max_length='50')),
                ('contrasena', models.TextField(max_length='100')),
            ],
        ),
    ]
