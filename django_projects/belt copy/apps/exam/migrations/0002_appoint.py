# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-23 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
