# Generated by Django 4.2.19 on 2025-04-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_remove_supplier_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryperson',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
