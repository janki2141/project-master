# Generated by Django 4.1.5 on 2023-01-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0015_remove_hosteldetail_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosteldetail',
            name='mobile',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]