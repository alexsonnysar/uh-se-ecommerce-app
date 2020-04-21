from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .forms import CheckoutForm
from .models import Item, Order, OrderItem, BillingAddress
from usps import USPSApi, Address

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"


class CheckoutView(View):
    def get(self, *args, **kwargs):
        #form
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, "checkout-page.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            street_address = form.cleaned_data.get('street_address')
            apartment_address = form.cleaned_data.get('apartment_address')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            same_billing_address = form.cleaned_data.get('same_billing_address')
            save_info = form.cleaned_data.get('save_info')

            print(street_address)
            print(country)


            return redirect('core:checkout')
        messages.warning(self.request, "Failed Checkout")
        return redirect('core:checkout')
         



class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, is_ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated ")

        else:
            messages.info(request, "This item was added to your cart.")
            order.items.add(order_item)
    else:
        date_ordered = timezone.now()
        order = Order.objects.create(user=request.user, date_ordered=date_ordered)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, is_ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed to your cart.")
            return redirect("core:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)

    else:
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)
