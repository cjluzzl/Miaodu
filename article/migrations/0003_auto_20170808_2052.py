# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-08 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articlecontent_new_or_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecontent',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/article/1/1.html', verbose_name='\u6587\u7ae0\u94fe\u63a5'),
        ),
    ]
