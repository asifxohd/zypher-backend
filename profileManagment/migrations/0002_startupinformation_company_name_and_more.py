# Generated by Django 5.0.4 on 2024-05-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileManagment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startupinformation',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startupinformation',
            name='contact_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='startupinformation',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]