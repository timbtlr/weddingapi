# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invite_name', models.CharField(max_length=20, null=True)),
                ('message', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invitee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('attending', models.BooleanField(default=False)),
                ('invitation', models.ForeignKey(related_name='invitees', to='rsvp.Invitation')),
            ],
        ),
    ]
