# Generated by Django 3.2.2 on 2022-08-30 03:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='length',
            field=models.DurationField(blank=True, default=datetime.timedelta, max_length=10),
        ),
    ]
