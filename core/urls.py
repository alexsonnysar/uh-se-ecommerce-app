from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    CheckoutView,
    add_to_cart,
    remove_from_cart,
    view_cart,
    remove_item_from_cart,
    order_confirmation,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("cart/", view_cart.as_view(), name="cart"),
    path("remove-from-cart/<slug>/", remove_from_cart, name="remove-from-cart"),
    path(
        "remove-item-from-cart/<slug>/",
        remove_item_from_cart,
        name="remove-item-from-cart",
    ),
    path(
        "order-confirmation/", order_confirmation.as_view(), name="order-confirmation"
    ),
]
