# Generated by Django 4.1.4 on 2023-02-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0021_foodmenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feestructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sno', models.CharField(max_length=100)),
                ('Details', models.CharField(max_length=100)),
                ('fee', models.CharField(max_length=100)),
            ],
        ),
    ]