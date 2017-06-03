# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-02 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugs',
            name='mechanism',
        ),
        migrations.AddField(
            model_name='drugs',
            name='admin_route',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drugs',
            name='entities',
            field=models.ManyToManyField(to='drugs.Entities'),
        ),
    ]