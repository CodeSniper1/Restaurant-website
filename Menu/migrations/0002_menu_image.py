# Generated by Django 4.2.5 on 2023-09-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='Menu/'),
        ),
    ]
