# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-22 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('employees', '0002_auto_20160721_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(blank=True, to='categories.Keyword'),
        ),
    ]