# Generated by Django 4.2.2 on 2023-07-08 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("problems", "0006_problem_hint"),
    ]

    operations = [
        migrations.AddField(
            model_name="problem",
            name="problem_initial",
            field=models.TextField(blank=True, null=True),
        ),
    ]
