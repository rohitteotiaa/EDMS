# Generated by Django 4.2.6 on 2023-10-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_basicuser_profile_pic_employee_profile_pic_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basicuser",
            name="profile_pic",
            field=models.ImageField(null=True, upload_to="media/profile_pic"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="profile_pic",
            field=models.ImageField(null=True, upload_to="media/profile_pic"),
        ),
        migrations.AlterField(
            model_name="users",
            name="profile_pic",
            field=models.ImageField(null=True, upload_to="media/profile_pic"),
        ),
    ]
