# Generated by Django 4.2.2 on 2023-07-08 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0002_alter_lesson_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lesson",
            name="context",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="description",
        ),
    ]
