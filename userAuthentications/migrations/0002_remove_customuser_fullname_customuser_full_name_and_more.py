# Generated by Django 5.0.4 on 2024-04-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fullName',
        ),
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('investor', 'Investor'), ('startup', 'Startup'), ('admin', 'Admin')], max_length=20),
        ),
    ]
