from django.conf import settings
from django.shortcuts import get_object_or_404
from flights.models import Voucher


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    voucher_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for voucher_id, quantity in shopping_bag.items():
        voucher = get_object_or_404(Voucher, pk=voucher_id)
        total += quantity * voucher.cost
        voucher_count += quantity
        shopping_bag_items.append({
            'voucher_id': voucher_id,
            'quantity': quantity,
            'voucher': voucher,
            'subtotal': quantity * voucher.cost,
        })

    grand_total = total

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'voucher_count': voucher_count,
        'grand_total': grand_total,
    }

    return context
