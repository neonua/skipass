# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipass', '0004_auto_20160628_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonement',
            name='bukovel_price',
            field=models.IntegerField(null=True, verbose_name='\u0412 \u043a\u0430\u0441\u0441\u0430\u0445 \u0411\u0443\u043a\u043e\u0432\u0435\u043b\u044f'),
        ),
        migrations.AlterField(
            model_name='abonement',
            name='hi_season',
            field=models.IntegerField(null=True, verbose_name='\u0412\u044b\u0441\u043e\u043a\u0438\u0439 \u0441\u0435\u0437\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='abonement',
            name='low_season',
            field=models.IntegerField(null=True, verbose_name='\u041d\u0438\u0437\u043a\u0438\u0439 \u0441\u0435\u0437\u043e\u043d'),
        ),
    ]
