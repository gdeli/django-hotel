# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_auto_20190528_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='photo',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
