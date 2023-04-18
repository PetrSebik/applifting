# Generated by Django 4.2 on 2023-04-18 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_id"),
        ("offer", "0002_apitoken"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="offers",
                to="product.product",
            ),
        ),
    ]
