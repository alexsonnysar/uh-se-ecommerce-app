from django.urls import path
from .views import HomeView, ItemDetailView, checkout, add_to_cart, remove_from_cart, view_cart

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    path("checkout/", checkout, name="checkout"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("cart/", view_cart.as_view(), name="add_view"),
    path("remove-from-cart/<slug>/", remove_from_cart, name="remove-from-cart"),
]
