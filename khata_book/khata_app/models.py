import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Khata_book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    client_name = models.CharField(max_length=200, null=True, blank=True)
    goods = models.CharField(max_length=150, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=False)
    size = models.DecimalField(decimal_places=3, max_digits=8, null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    created_on = models.DateField(null=True, blank=True, default=date.today())
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.client_name

