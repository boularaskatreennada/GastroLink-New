# Generated by Django 4.2.19 on 2025-04-16 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]
