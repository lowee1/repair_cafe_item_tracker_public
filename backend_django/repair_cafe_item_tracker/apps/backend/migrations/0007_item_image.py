# Generated by Django 4.2rc1 on 2023-04-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0006_remove_item_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
