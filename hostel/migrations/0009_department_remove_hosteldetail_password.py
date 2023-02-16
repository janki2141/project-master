# Generated by Django 4.1.4 on 2023-01-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0008_hosteldetail_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Field', models.CharField(max_length=50)),
                ('Semester', models.CharField(max_length=50)),
                ('Studentcode', models.CharField(max_length=50)),
                ('Timing', models.TimeField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='hosteldetail',
            name='password',
        ),
    ]