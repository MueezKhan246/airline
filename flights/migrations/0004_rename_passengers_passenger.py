# Generated by Django 3.2.6 on 2021-09-06 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20210906_0150'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]
