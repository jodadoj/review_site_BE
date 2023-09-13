from django.db import models
from django.contrib.auth import User, Group

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    stars = models.IntegerField()
    user = models.ForeignKey(USer, on_delete=models.CASCADE)
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    ordinal = models.IntegerField()

class Business(models.Model):
    LOW = "$"
    LOW_MID = "$$"
    MID = "$$$"
    HI_MID = "$$$$"
    HI = "$$$$$"

    name = models.CharField(max_length=255)
    description = models.TextField()
    price_range = models.CharField(max_length=10, 
                                   choices=PRICE_CHOICES)
    