# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('homepage', models.CharField(max_length=255)),
            ],
        ),
    ]
