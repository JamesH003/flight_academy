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
    }

    return render(request, template, context)