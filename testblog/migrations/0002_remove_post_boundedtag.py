# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='boundedtag',
        ),
    ]
