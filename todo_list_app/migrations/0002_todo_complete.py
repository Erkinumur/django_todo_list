# Generated by Django 2.2 on 2020-06-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
