# Generated by Django 5.1.1 on 2024-10-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0006_serialrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial',
            name='score',
            field=models.FloatField(),
        ),
    ]
