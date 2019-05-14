# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nama', models.CharField(max_length=50)),
                ('harga', models.CharField(max_length=50)),
                ('provinsi', models.CharField(max_length=50)),
                ('kota', models.CharField(max_length=50)),
                ('kodepos', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('rating', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=10, default='Male', choices=[('Male', 'Male'), ('Female', 'Female')]),
        ),
    ]
