# Generated by Django 5.0.4 on 2024-05-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0004_remove_gem_jewels_alter_jewelry_gem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Toy",
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
                ("name", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="gem",
            name="toys",
            field=models.ManyToManyField(to="main_app.toy"),
        ),
    ]
