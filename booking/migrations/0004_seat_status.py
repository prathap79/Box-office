# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-05 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20160731_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='status',
            field=models.CharField(choices=[(b'', b'Select'), (b'Processing', b'Processing'), (b'Available', b'Available'), (b'Ocupied', b'Occupied')], default=b'Available', max_length=10),
        ),
    ]
