# Generated by Django 2.1.5 on 2020-08-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20200816_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]