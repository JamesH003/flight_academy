from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from flights.models import Voucher
from shopping_bag.contexts import shopping_bag_contents

import stripe


def payments(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for voucher_id, item_data in shopping_bag.items():
                try:
                    voucher = Voucher.objects.get(id=voucher_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            voucher=voucher,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in item_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                voucher=voucher,
                                quantity=quantity,
                            )
                            order_line_item.save()
                except Voucher.DoesNotExist:
                    messages.error(request, ("One of the vouchers in your shopping bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_shopping_bag'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('payments_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check your information.')
    else:
        shopping_bag = request.session.get('shopping_bag', {})
        if not shopping_bag:
            messages.error(request, "Your shopping bag is currently empty")
            return redirect(reverse('vouchers'))

        current_shopping_bag = shopping_bag_contents(request)
        total = current_shopping_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )


        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    template = 'payments/payments.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)