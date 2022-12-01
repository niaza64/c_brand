from django.db import models

# Create your models here.
class cloth(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    count = models.IntegerField(blank=True, null=True)
    price= models.IntegerField(blank=True, null=True)

class cart(models.Model):
    name = models.CharField(max_length=30)
    price= models.IntegerField(blank=True, null=True)