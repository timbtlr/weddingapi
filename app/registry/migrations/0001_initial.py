# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('registry_url', models.CharField(max_length=200)),
                ('thumbnail_url', models.URLField()),
            ],
        ),
    ]
