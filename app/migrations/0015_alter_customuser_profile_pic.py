# Generated by Django 4.2.6 on 2023-10-31 04:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0014_remove_basicuser_profile_pic_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.FileField(upload_to="media/profile_pic"),
        ),
    ]
