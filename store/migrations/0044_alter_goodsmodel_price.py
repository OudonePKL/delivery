# Generated by Django 4.2.4 on 2024-08-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0043_alter_order_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goodsmodel",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=10, verbose_name="price"
            ),
        ),
    ]
