from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import (
    HomeView,
    ItemDetailView,
    CheckoutView,
    add_to_cart,
    remove_item_from_cart,
    CartView,
    item_quantity_reduction,
    OrderConfirmationView,
    MyOrdersViews,
)

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('core:home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_product_url_resolves(self):
        url = reverse('core:product', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, ItemDetailView)

    def test_checkout_url_reseolves(self):
        url = reverse('core:checkout')
        self.assertEquals(resolve(url).func.view_class, CheckoutView)
    
    