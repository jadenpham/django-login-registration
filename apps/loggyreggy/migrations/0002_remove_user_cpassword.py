# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-21 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loggyreggy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpassword',
        ),
    ]
