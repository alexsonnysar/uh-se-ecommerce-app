from django.urls import path
from .views import (
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

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("cart/", CartView.as_view(), name="cart"),
    path("remove-item-from-cart/<slug>/", remove_item_from_cart, name="remove-item-from-cart"),
    path(
        "item-quantity-reduction/<slug>/",
        item_quantity_reduction,
        name="item-quantity-reduction",
    ),
    path(
        "order-confirmation/", OrderConfirmationView.as_view(), name="order-confirmation"
    ),
    path("history/", MyOrdersViews.as_view(), name="history"),
]
