# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-07 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=50)),
                ('function', models.CharField(blank=True, max_length=50)),
                ('feature_name', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('rule_type', models.CharField(blank=True, choices=[('CHO', 'choice'), ('SEL', 'selection')], max_length=15)),
                ('option_min', models.IntegerField(blank=True, null=True)),
                ('option_max', models.IntegerField(blank=True, null=True)),
                ('enabled', models.NullBooleanField(default=False)),
                ('selected', models.NullBooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('dependency', models.ManyToManyField(related_name='dependent', to='fmm.Feature')),
            ],
        ),
    ]