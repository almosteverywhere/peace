# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-03 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0005_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attack',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='longitude',
            new_name='lng',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='longitude',
            new_name='lng',
        ),
    ]