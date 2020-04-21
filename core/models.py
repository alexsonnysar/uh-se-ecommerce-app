from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={"slug": self.slug})


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    date_created = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        "BillingAddress", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.user.username


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_adress = models.CharField(max_length=100)
    country = CountryField(multiple=True)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
