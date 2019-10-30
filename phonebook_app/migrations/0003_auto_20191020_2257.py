# Generated by Django 2.2.6 on 2019-10-20 19:57

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook_app', '0002_auto_20191020_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='job_title',
            field=models.CharField(default=datetime.datetime(2019, 10, 20, 19, 57, 46, 220462, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]