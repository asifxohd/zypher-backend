# Generated by Django 5.0.4 on 2024-05-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentications', '0009_alter_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='investorpreferences',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='investorpreferences',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]