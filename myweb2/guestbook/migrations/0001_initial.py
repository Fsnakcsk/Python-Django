# Generated by Django 4.1.1 on 2022-09-27 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gusstbook",
            fields=[
                ("idx", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("passwd", models.CharField(max_length=50)),
                ("content", models.TextField()),
                (
                    "post_date",
                    models.DateTimeField(blank=True, default=datetime.datetime),
                ),
            ],
        ),
    ]
