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
            name="beef", price=5, slug="beef", description="Texas Angus Beef",
        )

    def test_item_is_assigned_slug_on_creation(self):
        self.assertEquals(self.beef.slug, "beef")
