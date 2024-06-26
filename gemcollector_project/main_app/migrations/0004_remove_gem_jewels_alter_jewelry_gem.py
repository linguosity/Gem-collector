# Generated by Django 5.0.4 on 2024-05-07 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_alter_jewelry_options_gem_jewels"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gem",
            name="jewels",
        ),
        migrations.AlterField(
            model_name="jewelry",
            name="gem",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jewelry",
                to="main_app.gem",
            ),
        ),
    ]
