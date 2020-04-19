from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Item, Order, OrderItem

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'

def checkout(request):
    return render(request, 'checkout-page.html')

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, date_ordered=ordered_date)
        order.items.add(order_item)
    return redirect("core:product", slug=slug)

