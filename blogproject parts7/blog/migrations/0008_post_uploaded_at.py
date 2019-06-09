# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-08 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]