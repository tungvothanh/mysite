# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='Django/pythonanywhere/mysite/documents/%Y/%m/%d'),
        ),
    ]