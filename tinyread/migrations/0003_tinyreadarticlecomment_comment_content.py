# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-12 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyread', '0002_auto_20170812_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='tinyreadarticlecomment',
            name='comment_content',
            field=models.CharField(default='\u8bc4\u8bba', max_length=200, verbose_name='\u8bc4\u8bba\u5185\u5bb9'),
        ),
    ]
