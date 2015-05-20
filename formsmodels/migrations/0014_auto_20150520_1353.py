# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0013_auto_20150520_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singledriver',
            name='email',
            field=models.EmailField(default=b'me@pmtransport.com', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='internal_notes',
            field=models.TextField(default=b'none'),
        ),
    ]
