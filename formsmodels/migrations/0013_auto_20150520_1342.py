# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0012_auto_20150520_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodels',
            name='driver',
            field=models.ForeignKey(to='formsmodels.SingleDriver', to_field=b'license_no'),
        ),
        migrations.AlterField(
            model_name='singledriver',
            name='license_no',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
