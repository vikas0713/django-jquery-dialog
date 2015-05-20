# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0010_auto_20150520_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='internal_notes',
            field=models.TextField(default=b'none'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='ownership',
            field=models.CharField(default=b'Company Truck', max_length=100, choices=[(b'Company Truck', b'Company Truck'), (b'Other', b'Other')]),
        ),
    ]
