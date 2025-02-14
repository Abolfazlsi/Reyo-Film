# Generated by Django 5.1.1 on 2024-10-25 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0007_alter_serial_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerialEpisode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='serial_episodes')),
                ('episode_number', models.IntegerField()),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serial_episodes', to='serial.serial')),
            ],
        ),
    ]
