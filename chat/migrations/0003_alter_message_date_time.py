# Generated by Django 3.2.6 on 2021-10-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20211029_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
