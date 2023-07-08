# Generated by Django 4.2.2 on 2023-07-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trycode", "0003_remove_trycode_identification_trycode_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trycode",
            name="description",
            field=models.TextField(blank=True, default="", max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="trycode",
            name="intro",
            field=models.TextField(blank=True, default="", max_length=1000, null=True),
        ),
    ]