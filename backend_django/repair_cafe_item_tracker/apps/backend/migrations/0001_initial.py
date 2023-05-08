# Generated by Django 4.1.4 on 2022-12-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("item", models.TextField()),
                ("problem", models.TextField()),
                ("owner", models.TextField()),
                ("owner_email", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("status", models.TextField(default="Unassigned")),
                ("assigned_to", models.TextField(default="Unassigned")),
                ("difficulty", models.IntegerField(default=0)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
