# Generated by Django 4.2.6 on 2023-10-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0009_alter_customuser_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(null=True, upload_to="media/profile_pic"),
        ),
    ]