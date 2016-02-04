# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20151210_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 11, 29, 31, 10000, tzinfo=utc)),
        ),
    ]
