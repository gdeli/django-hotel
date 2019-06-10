# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20190526_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='date',
            field=models.DateTimeField(default='2012-09-04 06:00:00.000000-08:00', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='rating',
            field=models.FloatField(default=1, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
