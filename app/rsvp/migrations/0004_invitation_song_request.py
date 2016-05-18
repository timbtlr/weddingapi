# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_auto_20160518_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='song_request',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
