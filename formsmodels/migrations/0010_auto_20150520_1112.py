# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0009_auto_20150520_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodels',
            name='status',
            field=models.CharField(default=b'Opened', max_length=50, choices=[(b'Opened', b'Opened'), (b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Complete', b'Complete'), (b'Loaded', b'Loaded'), (b'Unloaded', b'Unloaded'), (b'Free', b'Free'), (b'OnRoute', b'OnRoute'), (b'InYard', b'InYard'), (b'Delivered', b'Delivered'), (b'Covered', b'Covered')]),
        ),
        migrations.AlterField(
            model_name='singledriver',
            name='internal_notes',
            field=models.TextField(default=b'none'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='ownership',
            field=models.CharField(default=b'Company Truck', max_length=100, choices=[(b'Company Truck', b'Company Truck'), (b'Other', b'Other')]),
        ),
    ]
