from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile

from payments.models import Order


@login_required
def user_profile(request):
    """ Display the user's profile """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    orders = user_profile.orders.all()

    template = 'user_profile/user_profile.html'
    context = {
        'user_profile': user_profile,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'payments/payments_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
