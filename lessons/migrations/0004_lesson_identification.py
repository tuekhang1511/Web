# Generated by Django 4.2.2 on 2023-07-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0003_remove_lesson_context_remove_lesson_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="identification",
            field=models.IntegerField(default=0),
        ),
    ]