from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1)
    description = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.name