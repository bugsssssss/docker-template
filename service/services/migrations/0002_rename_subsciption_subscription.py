# Generated by Django 3.2.16 on 2023-07-17 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subsciption',
            new_name='Subscription',
        ),
    ]
