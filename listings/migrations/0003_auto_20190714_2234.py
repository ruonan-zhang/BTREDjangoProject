# Generated by Django 2.2.1 on 2019-07-15 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190714_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='adress',
            new_name='address',
        ),
    ]
