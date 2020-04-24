from django.test import TestCase
from allauth.utils import get_user_model
from core.models import (
    Item,
    OrderItem,
    Order,
    BillingAddress,
)


class TestModels(TestCase):
    def setUp(self):
        self.beef = Item.objects.create(
            name="beef",
            price=5,
            slug="beef",
            picture="some-link",
            description="Texas Angus Beef",
        )
        self.order_item = OrderItem.objects.create(
            user=get_user_model().objects.create(username="@raymond.penners"),
            item=self.beef,
            quantity=4,
            is_ordered=False,
        )
        self.order_item = OrderItem.objects.create(
            user=get_user_model().objects.create(username="@raymond.penners"),
            item=self.beef,
            quantity=4,
            is_ordered=False,
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
