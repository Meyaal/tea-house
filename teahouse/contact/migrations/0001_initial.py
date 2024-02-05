# Generated by Django 3.2.20 on 2023-09-22 06:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
                ("subject", models.CharField(max_length=230)),
                ("message", models.TextField(max_length=2000)),
                ("date", models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
