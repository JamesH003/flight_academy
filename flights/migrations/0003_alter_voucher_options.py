# Generated by Django 3.2.23 on 2024-02-05 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_alter_aircraft_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voucher',
            options={'ordering': ['aircraft_type']},
        ),
    ]
