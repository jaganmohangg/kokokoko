# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-08 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_uploaded_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DjangoDocument',
        ),
        migrations.DeleteModel(
            name='MachinelearningDocument',
        ),
        migrations.DeleteModel(
            name='PythonDocument',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
