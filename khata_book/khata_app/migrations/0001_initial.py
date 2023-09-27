# Generated by Django 4.2.5 on 2023-09-25 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Khata_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=200, null=True)),
                ('goods', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(blank=True, max_length=10, null=True)),
                ('price', models.IntegerField(max_length=12, null=True)),
                ('size', models.IntegerField(blank=True, max_length=8, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
