# Generated by Django 5.0.6 on 2024-08-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_maturity_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
