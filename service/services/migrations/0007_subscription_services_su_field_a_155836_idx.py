# Generated by Django 3.2.16 on 2023-07-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20230726_0740'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='subscription',
            index=models.Index(fields=['field_a', 'field_b'], name='services_su_field_a_155836_idx'),
        ),
    ]