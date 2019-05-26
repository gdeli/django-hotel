# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20190524_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='rating',
            field=models.FloatField(default=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='ratinghotel',
            field=models.ForeignKey(default=1, blank=True, to='hotel.Hotel'),
            preserve_default=False,
        ),
    ]
