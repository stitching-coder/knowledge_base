# Generated by Django 5.1.5 on 2025-01-26 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happiness', '0003_alter_wordoftheyear_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordoftheyear',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 26, 22, 25, 26, 294801, tzinfo=datetime.timezone.utc)),
        ),
    ]
