# Generated by Django 4.2.4 on 2023-11-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_superuser_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='superuser_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Message',
            new_name='superuser_basicuser',
        ),
    ]
