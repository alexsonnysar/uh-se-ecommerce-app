from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
        # form
        form = CheckoutForm()
        context = {"form": form}
        return render(self.request, "checkout-page.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            street_address = form.cleaned_data.get("street_address")
            country = form.cleaned_data.get("country")
            state = form.cleaned_data.get("state")
            city = form.cleaned_data.get("city")
            zip = form.cleaned_data.get("zip")
            same_billing_address = form.cleaned_data.get("same_billing_address")
            save_info = form.cleaned_data.get("save_info")

            address = Address(
                name=name,
                address_1=street_address,
                city=city,
                state=state,
                zipcode=zip,
            )

            usps = USPSApi("097UNIVE5841", test=True)
            validation = usps.validate_address(address)
            try:
                valid = validation.result["AddressValidateResponse"]["Address"][
                    "Address1"
                ]
                billing_address = BillingAddress(
                    user=self.request.user,
                    street_adress=street_address,
                    country=country,
                    state=state,
                    city=city,
                    zip=zip,
                )
                existingaddress = BillingAddress.objects.filter(
                    user=self.request.user
                ).count()
                if existingaddress != 0:
                    BillingAddress.objects.filter(user=self.request.user).delete()
                    billing_address.save()
                    return redirect("core:order-confirmation")
                else:
                    billing_address.save()
                    return redirect("core:order-confirmation")
            except:
                messages.warning(self.request, "Not a Valid Address")

            return redirect("core:checkout")
        messages.warning(self.request, "Failed Checkout")
        return redirect("core:checkout")


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"


@login_required
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
            return redirect("core:cart")

        else:
            messages.info(request, "This item was added to your cart.")
            order.items.add(order_item)
            return redirect("core:cart")
    else:
        date_ordered = timezone.now()
        order = Order.objects.create(user=request.user, date_ordered=date_ordered)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:cart")


@login_required
def remove_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, is_ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:cart")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)

    else:
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)


@login_required
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
            order_item.delete()
            messages.info(request, "This item was removed to your cart.")
            return redirect("core:cart")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)

    else:
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)


class view_cart(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            context = {"object": order}
            return render(self.request, "cart.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


class order_confirmation(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            qs = Order.objects.filter(user=self.request.user, is_ordered=False)
            billing = BillingAddress.objects.get(user=self.request.user)
            context = {"object": order, "object2": billing, "user": self.request.user}
            qs.update(is_ordered=True)
            return render(self.request, "order-confirmation.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


class Previous_Orders(DetailView):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.filter(user=self.request.user, is_ordered=True)
            context = {"object": order}
            return render(self.request, "history.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have any previous orders")
            return redirect("/")