# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-08 05:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_auto_20170908_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdate',
            name='tourdatetime',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
