# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipass', '0010_auto_20160722_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonement',
            name='name',
            field=models.IntegerField(max_length=128, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043d\u0435\u0439'),
        ),
    ]