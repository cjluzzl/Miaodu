# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-08 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20170808_2052'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
