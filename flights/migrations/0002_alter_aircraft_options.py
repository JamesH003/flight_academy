# Generated by Django 3.2.23 on 2024-01-31 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aircraft',
            options={'ordering': ['aircraft_type'], 'verbose_name_plural': 'Aircraft'},
        ),
    ]
