# Generated by Django 4.2.5 on 2023-09-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='availabilityTime',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
