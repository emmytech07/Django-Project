# Generated by Django 3.2.8 on 2022-04-18 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventor',
            name='is_inventor',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='is_investor',
        ),
    ]
