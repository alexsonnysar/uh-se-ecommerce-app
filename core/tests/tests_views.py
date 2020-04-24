from django.test import TestCase, Client
from django.urls import reverse
from core.models import (
    Item,
    OrderItem,
    Order,
    BillingAddress,
)
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('core:home')
        self.checkout_url = reverse('core:checkout')
        self.item_detail_url = reverse('core:product', args=["beef"])
        Item.objects.create(
            name='beef',
            price=5
        )

    def test_home_view_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home-page.html')

    def test_checkout_view_GET(self):
        response = self.client.get(self.checkout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout-page.html')

    def test_item_detail_view_GET(self):
        response = self.client.get(self.item_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product-page.html')
    


