# Generated by Django 5.1.1 on 2024-11-07 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_genre_blog_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcontent',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_contents', to='blog.blog'),
        ),
    ]
