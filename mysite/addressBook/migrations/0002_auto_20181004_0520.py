# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('addressBook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
