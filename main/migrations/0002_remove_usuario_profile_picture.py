# Generated by Django 5.1.4 on 2025-01-02 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='profile_picture',
        ),
    ]