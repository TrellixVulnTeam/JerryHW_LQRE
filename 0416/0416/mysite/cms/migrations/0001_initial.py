# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-22 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('birthday', models.DateTimeField(default=django.utils.timezone.now, verbose_name='出生日期')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=2)),
            ],
        ),
    ]