# Generated by Django 5.1.5 on 2025-01-27 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HabitEntry',
            new_name='Habit',
        ),
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name_plural': 'Habits'},
        ),
    ]
