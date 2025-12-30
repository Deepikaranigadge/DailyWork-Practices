from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='Cloths')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.TextField(default='')

def __str__(self):
    return self.title
    
