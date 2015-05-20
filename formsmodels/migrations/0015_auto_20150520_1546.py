# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0014_auto_20150520_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodels',
            name='driver',
            field=models.ForeignKey(to='formsmodels.SingleDriver', blank=True, to_field=b'license_no'),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='trailer',
            field=models.ForeignKey(to='formsmodels.Trailer', blank=True, to_field=b'trailer_no'),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='truck',
            field=models.ForeignKey(to='formsmodels.Truck', blank=True, to_field=b'truck_no'),
        ),
        migrations.AlterField(
            model_name='singledriver',
            name='email',
            field=models.EmailField(default=b'me@pm.com', max_length=254, null=True),
        ),
    ]
