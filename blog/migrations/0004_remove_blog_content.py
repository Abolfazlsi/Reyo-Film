# Generated by Django 5.1.1 on 2024-11-07 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcontent_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]