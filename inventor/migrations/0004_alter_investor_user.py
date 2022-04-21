# Generated by Django 3.2.8 on 2022-04-19 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0003_auto_20220418_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investor', to=settings.AUTH_USER_MODEL),
        ),
    ]
