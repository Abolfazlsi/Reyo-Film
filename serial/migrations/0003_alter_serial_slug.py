# Generated by Django 5.1.1 on 2024-10-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0002_serial_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]
