# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_reviewer_ratinghotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='ratinghotel',
            field=models.ForeignKey(blank=True, null=True, to='hotel.Hotel'),
        ),
    ]
