# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20160518_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitee',
            name='attending',
            field=models.NullBooleanField(default=None),
        ),
    ]
