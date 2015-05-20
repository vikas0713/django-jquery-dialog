# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0011_auto_20150520_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodels',
            name='trailer',
            field=models.ForeignKey(to='formsmodels.Trailer', to_field=b'trailer_no'),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='truck',
            field=models.ForeignKey(to='formsmodels.Truck', to_field=b'truck_no'),
        ),
    ]
