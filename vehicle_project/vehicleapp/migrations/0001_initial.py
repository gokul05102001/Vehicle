# Generated by Django 4.2.1 on 2023-07-19 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('company', models.CharField(max_length=250)),
                ('cc', models.IntegerField()),
                ('features', models.TextField()),
            ],
        ),
    ]
