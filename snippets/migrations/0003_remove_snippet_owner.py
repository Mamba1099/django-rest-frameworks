# Generated by Django 3.2.12 on 2024-01-03 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20240102_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
    ]