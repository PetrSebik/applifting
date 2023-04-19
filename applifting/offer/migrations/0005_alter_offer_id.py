# Generated by Django 4.2 on 2023-04-19 13:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0004_alter_offer_items_in_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="id",
            field=models.UUIDField(
                db_index=True, default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
