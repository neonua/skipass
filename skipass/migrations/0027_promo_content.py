# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-13 10:47
from __future__ import unicode_literals

import datetime
from django.db import migrations
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('skipass', '0026_auto_20160912_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='content',
            field=tinymce.models.HTMLField(default=datetime.datetime(2016, 9, 13, 10, 47, 18, 718341, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
