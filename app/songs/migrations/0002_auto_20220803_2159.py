# Generated by Django 3.2.2 on 2022-08-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='disc_number',
            field=models.PositiveSmallIntegerField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='songs',
            name='track_number',
            field=models.PositiveSmallIntegerField(blank=True, default=''),
        ),
    ]