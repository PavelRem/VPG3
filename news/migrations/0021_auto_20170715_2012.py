# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AddField(
            model_name='newsdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsdata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
