# Generated by Django 4.2.6 on 2024-02-05 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diplom", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="deliverTo",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2024, 2, 5, 12, 59, 58, 263171),
                verbose_name="Доставить до",
            ),
        ),
    ]