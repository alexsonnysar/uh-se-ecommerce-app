from django.test import TestCase, Client
from django.conf import settings
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
        self.cart_url = reverse('core:cart')
        self.order_confirmation_url = reverse('core:order-confirmation')
        self.my_orders_url = reverse('core:history')
        self.beef = Item.objects.create(
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

    def test_checkout_view_POST(self):
        pass

    def test_item_detail_view_GET(self):
        response = self.client.get(self.item_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product-page.html')

    def test_add_to_cart(self):
        pass

    def test_item_quantity_reduction(self):
        pass

    def test_remove_item_from_cart(self):
        pass
    
    def test_cart_view_GET_with_order(self):
        pass
        # response = self.client.get(self.cart_url)

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'cart.html')

    def test_cart_view_GET_no_order(self):
        response = self.client.get(self.cart_url)

        self.assertEquals(response.status_code, 302)

    def test_order_confirmation_view_GET_with_order(self):
        pass

    def test_order_confirmation_view_GET_no_order(self):
        pass
        # response = self.client.get(self.order_confirmation_url)

        # self.assertEquals(response.status_code, 302)

    def test_my_orders_view_GET_with_order(self):
        pass
    
    def test_my_orders_view_GET_no_order(self):
        pass
        # response = self.client.get(self.my_orders_url)

        # self.assertEquals(response.status_code, 302)


