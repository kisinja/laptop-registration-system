# Generated by Django 5.0 on 2024-02-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0007_laptop_created_laptop_modified_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="contact_info",
        ),
        migrations.RemoveField(
            model_name="student",
            name="grade",
        ),
        migrations.RemoveField(
            model_name="student",
            name="student_id",
        ),
        migrations.AddField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female")],
                max_length=255,
                null=True,
            ),
        ),
    ]
