# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-09-29 17:27
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('netjsongraph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='status',
            field=model_utils.fields.StatusField(default='up', max_length=100, no_check_for_status=True),
        ),
    ]
