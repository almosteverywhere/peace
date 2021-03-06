# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-02 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0003_auto_20161002_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='attack',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
    ]
