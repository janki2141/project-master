# Generated by Django 4.1.4 on 2023-02-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0029_stuentery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuattendance',
            name='ABSENT',
            field=models.BooleanField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stuattendance',
            name='PRESENT',
            field=models.BooleanField(max_length=100),
        ),
    ]
