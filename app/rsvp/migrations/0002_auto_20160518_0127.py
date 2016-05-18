# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitee',
            name='attending',
            field=models.BooleanField(default=None),
        ),
    ]
