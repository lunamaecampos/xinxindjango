# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-08 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_auto_20170908_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourdate',
            name='tourdatetime',
            field=models.DateTimeField(),
        ),
    ]
