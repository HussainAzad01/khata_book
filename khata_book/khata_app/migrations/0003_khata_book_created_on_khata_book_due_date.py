# Generated by Django 4.2.5 on 2023-09-25 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khata_app', '0002_alter_khata_book_price_alter_khata_book_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='khata_book',
            name='created_on',
            field=models.DateField(blank=True, default=datetime.date(2023, 9, 25), null=True),
        ),
        migrations.AddField(
            model_name='khata_book',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
