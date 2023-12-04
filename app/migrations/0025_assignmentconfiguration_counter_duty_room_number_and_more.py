# Generated by Django 4.2.4 on 2023-11-09 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_user_basicuser_user_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('room_number', models.CharField(max_length=100)),
                ('counter_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='room_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('emp_Code', models.CharField(default='None', max_length=100)),
                ('gender', models.CharField(default='None', max_length=100)),
                ('contact', models.CharField(default='None', max_length=10)),
                ('address', models.CharField(default='None', max_length=200)),
                ('working_location', models.CharField(default='None', max_length=100)),
                ('counter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.counter')),
                ('room_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.room_number')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.section')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.zone')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.counter')),
                ('duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.duty')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.member')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room_number')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.section')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.zone')),
            ],
        ),
    ]