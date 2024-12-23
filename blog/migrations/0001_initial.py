# Generated by Django 5.1.1 on 2024-11-07 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('blog_image', models.ImageField(upload_to='blogcontent_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog_image')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog.blogcontent')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog.bloggenre')),
            ],
        ),
    ]
