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
        url = reverse("core:home")
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_product_url_resolves(self):
        url = reverse("core:product", args=["some-slug"])
        self.assertEqual(resolve(url).func.view_class, ItemDetailView)

    def test_checkout_url_reseolves(self):
        url = reverse("core:checkout")
        self.assertEquals(resolve(url).func.view_class, CheckoutView)

    def test_add_to_cart_url(self):
        url = reverse("core:add-to-cart", args=["some slug"])
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_remove_item_from_cart_url(self):
        url = reverse("core:remove-item-from-cart", args=["some-slug"])
        self.assertEqual(resolve(url).func, remove_item_from_cart)

    def test_cart_view_url(self):
        url = reverse("core:cart")
        self.assertEquals(resolve(url).func.view_class, CartView)

    def test_item_quantity_reduction_url(self):
        url = reverse("core:item-quantity-reduction", args=["some=slug"])
        self.assertEquals(resolve(url).func, item_quantity_reduction)

    def test_order_confirmation_url(self):
        url = reverse("core:order-confirmation")
        self.assertEqual(resolve(url).func.view_class, OrderConfirmationView)

    def test_my_order_url(self):
        url = reverse("core:history")
        self.assertEquals(resolve(url).func.view_class, MyOrdersViews)
