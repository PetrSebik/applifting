# Generated by Django 4.2 on 2023-04-17 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.UUIDField(db_index=True, primary_key=True, serialize=False),
                ),
                ("price", models.IntegerField()),
                ("items_in_stock", models.CharField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_offer",
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]