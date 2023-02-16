# Generated by Django 4.1.4 on 2022-12-28 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostel', '0002_delete_tab'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentcode', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100, null=True)),
                ('native', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('joiningdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
