# Generated by Django 3.2.23 on 2024-02-07 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20240205_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licence',
            name='required_flight_time',
            field=models.PositiveIntegerField(default=30, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(1500)]),
        ),
    ]