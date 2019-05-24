# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20190522_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rating', models.CharField(max_length=9, default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
                ('review', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='review',
        ),
    ]
