# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20190522_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(max_length=9, default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
