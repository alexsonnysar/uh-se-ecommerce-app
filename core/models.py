from django.conf import settings
from django.db import models
from django.shortcuts import reverse

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("core:product", kwargs ={
            'slug': self.slug
        })


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    date_created = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username