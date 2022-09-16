from unicodedata import name
from django.db import models
from users.models import CustomUser
# Create your models here.
class Cap(models.Model):
    name = models.TextField(max_length=50, default='')
    image = models.ImageField(upload_to='savedImages')
    desc = models.TextField(max_length=500)
    price = models.IntegerField()
    qty_sold = models.IntegerField(default=0)
    
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cap = models.ForeignKey(Cap, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()

from django.contrib import admin

admin.site.register(Cap)