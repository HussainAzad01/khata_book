# Generated by Django 4.2.5 on 2023-09-26 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khata_app', '0004_rename_total_price_khata_book_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khata_book',
            name='created_on',
            field=models.DateField(blank=True, default=datetime.date(2023, 9, 26), null=True),
        ),
        migrations.AlterField(
            model_name='khata_book',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]