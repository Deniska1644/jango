# Generated by Django 4.2.7 on 2023-11-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
