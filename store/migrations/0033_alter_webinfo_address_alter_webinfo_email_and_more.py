# Generated by Django 4.2.4 on 2024-07-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0032_remove_webinfo_background_webinfo_banner1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webinfo",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webinfo",
            name="email",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webinfo",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webinfo",
            name="tel1",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="webinfo",
            name="tel2",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
