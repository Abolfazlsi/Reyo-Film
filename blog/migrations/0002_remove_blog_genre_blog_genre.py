# Generated by Django 5.1.1 on 2024-11-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='genre',
        ),
        migrations.AddField(
            model_name='blog',
            name='genre',
            field=models.ManyToManyField(related_name='blogs', to='blog.bloggenre'),
        ),
    ]
