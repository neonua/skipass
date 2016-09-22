# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-12 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skipass', '0025_auto_20160912_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementhight',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='season_hight', to='skipass.Seasons', verbose_name='C\u0435\u0437\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='abonementlow',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='season_low', to='skipass.Seasons', verbose_name='C\u0435\u0437\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='clubcartpay',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='season', to='skipass.Seasons', verbose_name='C\u0435\u0437\u043e\u043d'),
        ),
    ]