# Generated by Django 4.2.5 on 2023-09-23 16:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('dateTime', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('peoples', models.IntegerField()),
                ('specialrequest', models.TextField()),
            ],
        ),
    ]
