# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20190523_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='ratinghotel',
            field=models.ForeignKey(default=1, to='hotel.Hotel'),
            preserve_default=False,
        ),
    ]
