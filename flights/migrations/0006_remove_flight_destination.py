# Generated by Django 3.2.20 on 2023-07-18 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='destination',
        ),
    ]
