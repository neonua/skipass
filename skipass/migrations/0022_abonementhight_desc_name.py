# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-12 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipass', '0021_auto_20160912_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementhight',
            name='desc_name',
            field=models.CharField(blank=True, max_length=32, verbose_name='\u0414\u043d\u0438 \u0434\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f'),
        ),
    ]
