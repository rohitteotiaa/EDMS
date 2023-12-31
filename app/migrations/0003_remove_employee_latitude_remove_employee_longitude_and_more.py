# Generated by Django 4.2.6 on 2023-10-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_employee_basicuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="longitude",
        ),
        migrations.AddField(
            model_name="employee",
            name="contact_number",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="employee",
            name="pno_number",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="basicuser",
            name="latitude",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="basicuser",
            name="longitude",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
