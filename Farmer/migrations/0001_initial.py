# Generated by Django 4.1.5 on 2023-01-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='SellerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=11)),
            ],
        ),
    ]
