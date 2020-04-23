from django import template
from core.models import Order

register = template.Library()


@register.filter
def get_cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, is_ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0


@register.filter
def get_name(user):
    if user.is_authenticated:
        return user.username
