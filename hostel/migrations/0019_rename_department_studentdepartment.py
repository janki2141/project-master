# Generated by Django 4.1.5 on 2023-02-02 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0018_department_fullname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='department',
            new_name='studentdepartment',
        ),
    ]