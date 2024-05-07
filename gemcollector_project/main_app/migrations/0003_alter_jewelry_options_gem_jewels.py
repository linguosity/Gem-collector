# Generated by Django 5.0.4 on 2024-05-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_jewelry"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jewelry",
            options={},
        ),
        migrations.AddField(
            model_name="gem",
            name="jewels",
            field=models.ManyToManyField(related_name="gems", to="main_app.jewelry"),
        ),
    ]
