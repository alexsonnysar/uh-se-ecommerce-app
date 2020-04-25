from django.test import TestCase
from allauth.utils import get_user_model
from datetime import datetime
from django_countries.fields import CountryField
from django.utils.encoding import force_str

from core.models import (
    Item,
    OrderItem,
    Order,
    BillingAddress,
)


class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="@raymond.penners")
        self.beef = Item.objects.create(
            name="beef",
            price=5,
            slug="beef",
            picture="some-link",
            description="Texas Angus Beef",
        )
        self.billing_address = BillingAddress.objects.create(
            user=self.user,
            street_address="123 blah",
            country="US",
            state="TX",
            city="Houston",
            zip="12345"
        )
        self.order_item = OrderItem.objects.create(
            user=self.user,
            item=self.beef,
            quantity=4,
            is_ordered=False,
        )
        self.order_item2 = OrderItem.objects.create(
            user=self.user,
            item=self.beef,
            quantity=1,
            is_ordered=False,
        )
        self.order = Order.objects.create(
            user=self.user,
            date_created= "2020-04-23 20:52:20.709205",
            date_ordered= "2020-04-23 20:52:20.709205",
            is_ordered=False,
            billing_address=self.billing_address
        )

    def test_item_is_assigned_attributes_on_creation(self):
        self.assertEquals(self.beef.name, "beef")
        self.assertEquals(self.beef.price, 5)
        self.assertEquals(self.beef.picture, "some-link")
        self.assertEquals(self.beef.description, "Texas Angus Beef")

    def test_order_item_is_assigned_attributes_on_creation(self):
        self.assertEquals(self.order_item.user.username, "@raymond.penners")
        self.assertEquals(self.order_item.item, self.beef)
        self.assertEquals(self.order_item.quantity, 4)
        self.assertEquals(self.order_item.is_ordered, False)

    def test_order_is_assigned_attributes_on_creation(self):
        self.assertEquals(self.order.user.username, "@raymond.penners")

    def test_billing_address_is_assigned_attributes_on_creation(self):
        self.assertEquals(self.billing_address.user.username, "@raymond.penners")
        self.assertEquals(self.billing_address.street_address, "123 blah")
        self.assertEquals(self.billing_address.city, "Houston")
        self.assertEquals(self.billing_address.zip, "12345")
