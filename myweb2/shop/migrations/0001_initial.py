# Generated by Django 4.1.1 on 2022-09-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("cart_id", models.AutoField(primary_key=True, serialize=False)),
                ("userid", models.CharField(max_length=150)),
                ("product_id", models.IntegerField(default=0)),
                ("amount", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=150)),
                ("price", models.IntegerField(default=0)),
                ("description", models.TextField(max_length=150)),
                ("picture_url", models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
