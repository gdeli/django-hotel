# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_auto_20190526_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='rating',
            field=models.FloatField(default=1, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
    ]
