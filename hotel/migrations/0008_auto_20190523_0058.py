# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20190523_0040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review',
            new_name='reviewer',
        ),
    ]
