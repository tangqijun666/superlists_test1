# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-27 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='', verbose_name='内容'),
        ),
    ]
