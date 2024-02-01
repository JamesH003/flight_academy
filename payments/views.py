from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def payments(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "Your shopping bag is currently empty")
        return redirect(reverse('vouchers'))

    order_form = OrderForm()
    template = 'payments/payments.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Of1FzFIBeo32zW9gNHC9Qqda1a55dVuvm9wunbKXFSbM1miigw4vYXQ75sio78eJFrfpYZtjJjDYO74xJkuhLhr00zyFHzPcQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)