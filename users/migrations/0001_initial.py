# Generated by Django 2.2.1 on 2019-06-04 05:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('roll', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=50)),
                ('hall', models.CharField(max_length=15)),
                ('room', models.CharField(max_length=20)),
                ('blood_group', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=10)),
                ('hometown', models.CharField(max_length=100)),
                ('fblink', models.URLField(max_length=120)),
                ('por', django.contrib.postgres.fields.jsonb.JSONField()),
                ('earlier_login', models.BooleanField()),
            ],
        ),
    ]