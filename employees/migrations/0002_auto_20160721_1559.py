# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-21 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ManyToManyField(blank=True, to='employees.Role'),
        ),
    ]