# Generated by Django 2.1.5 on 2020-08-24 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='first_visit',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 24, 15, 44, 35, 948865, tzinfo=utc)),
        ),
    ]
