# Generated by Django 5.1.5 on 2025-01-27 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stitching', '0002_stitchingprojectentry_image_filename_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('stitching_type', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('tags', models.CharField(blank=True, max_length=200)),
                ('image_filename', models.CharField(default='image.jpg', max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2025, 1, 27, 13, 6, 10, 478504, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.DeleteModel(
            name='StitchingProjectEntry',
        ),
    ]
