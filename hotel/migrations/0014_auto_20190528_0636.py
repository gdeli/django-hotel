# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_auto_20190528_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
