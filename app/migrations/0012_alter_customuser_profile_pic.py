# Generated by Django 4.2.6 on 2023-10-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0011_rename_employee_superuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(default="", upload_to="media/profile_pic"),
        ),
    ]