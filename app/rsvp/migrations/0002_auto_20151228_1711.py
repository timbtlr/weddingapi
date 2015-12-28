# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='invite_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='invitee',
            name='invitation',
            field=models.ForeignKey(related_name='invitees', to='rsvp.Invitation'),
        ),
    ]
