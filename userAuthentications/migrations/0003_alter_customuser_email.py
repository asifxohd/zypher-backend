# Generated by Django 5.0.4 on 2024-04-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentications', '0002_remove_customuser_fullname_customuser_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=300, unique=True),
        ),
    ]