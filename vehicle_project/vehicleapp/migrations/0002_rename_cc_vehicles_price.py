# Generated by Django 4.2.1 on 2023-07-19 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicles',
            old_name='cc',
            new_name='price',
        ),
    ]