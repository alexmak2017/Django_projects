# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_websitesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesettings',
            name='favicon',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]