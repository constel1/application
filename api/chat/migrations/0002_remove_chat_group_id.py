# Generated by Django 4.2 on 2023-05-11 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='group_id',
        ),
    ]
