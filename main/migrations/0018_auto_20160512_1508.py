# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20160512_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(default='', path='~/Descargas'),
        ),
    ]
