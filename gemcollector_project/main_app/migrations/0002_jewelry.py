# Generated by Django 5.0.4 on 2024-05-05 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Jewelry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("url", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=250)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("W", "Watch"),
                            ("E", "Earrings"),
                            ("R", "Ring"),
                            ("B", "Bracelet"),
                            ("N", "Necklace"),
                        ],
                        default="W",
                        max_length=1,
                    ),
                ),
                (
                    "gem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main_app.gem"
                    ),
                ),
            ],
            options={
                "ordering": ["-price"],
            },
        ),
    ]