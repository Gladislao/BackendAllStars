# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-25 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_password_reset_required',
            field=models.BooleanField(default=True),
        ),
    ]
