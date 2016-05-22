# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0004_invitation_song_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitee',
            name='timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
