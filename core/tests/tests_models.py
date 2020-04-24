from django.test import TestCase
from core.models import (
    Item,
    OrderItem,
    Order,
    BillingAddress,
)


class TestModels(TestCase):
    def setUp(self):
        self.beef = Item.objects.create(
            name="beef", price=5, slug="beef", picture="some-link", description="Texas Angus Beef",
        )
        # self.order_item = OrderItem.objects.create(

        # )

    def test_item_is_assigned_attributes_on_creation(self):
        self.assertEquals(self.beef.name, "beef")
        self.assertEquals(self.beef.price, 5)
        self.assertEquals(self.beef.picture, "some-link")
        self.assertEquals(self.beef.description, "Texas Angus Beef")

    def test_order_item_is_assigned_attributes_on_creation(self):
        pass
