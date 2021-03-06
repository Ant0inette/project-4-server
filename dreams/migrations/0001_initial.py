# Generated by Django 3.2.4 on 2021-06-19 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('characters', models.CharField(max_length=60)),
                ('settings', models.CharField(max_length=60)),
                ('emotions', models.CharField(max_length=60)),
                ('themes', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=6000)),
                ('caption', models.CharField(max_length=60)),
                ('image_url', models.CharField(max_length=800)),
                ('coherence_rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]
