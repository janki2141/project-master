# Generated by Django 4.1.4 on 2023-02-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0031_delete_sturoom'),
    ]

    operations = [
        migrations.CreateModel(
            name='studroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STUNAME', models.CharField(max_length=100)),
                ('ROOMNO', models.CharField(max_length=100)),
                ('BEDNO', models.CharField(max_length=100)),
                ('MEMBERS', models.CharField(max_length=100)),
                ('TABLE', models.CharField(max_length=100)),
                ('CHAIR', models.CharField(max_length=100)),
                ('CUPBOARD', models.CharField(max_length=100)),
            ],
        ),
    ]
