# Generated by Django 4.2.7 on 2023-11-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('time_registr', models.DateField()),
            ],
        ),
    ]