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
    def set_up(self):
        self.client = Client()
        self.home_url = reverse('core:home')

    def test_item_list_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home-page.html')