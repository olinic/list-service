# Generated by Django 4.2.6 on 2023-10-23 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='user',
        ),
    ]
