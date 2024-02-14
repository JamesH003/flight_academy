from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse)
from django.contrib import messages

from flights.models import Voucher


# view to view the shopping bag
def view_shopping_bag(request):
    """ A view that renders the shopping bag contents page """

    return render(request, 'shopping_bag/shopping_bag.html')


# view to add vouchers to the shopping bag
def add_to_shopping_bag(request, voucher_id):
    """ Add a quantity of the specified voucher to the shopping bag """

    voucher = get_object_or_404(Voucher, pk=voucher_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if voucher_id in list(shopping_bag.keys()):
        shopping_bag[voucher_id] += quantity
        messages.success(
            request,
            f'Updated {voucher.title} quantity to {voucher.title} '
            f'quantity to {shopping_bag[voucher_id]}'
        )
    else:
        shopping_bag[voucher_id] = quantity
        messages.success(
            request, f'Added {voucher.title} to your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


# view to adjust the quantity of vouchers in the shopping bag
def adjust_shopping_bag(request, voucher_id):
    """ Adjust the quantity of the specified voucher in the shopping bag """

    shopping_bag = request.session.get('shopping_bag', {})
    voucher = get_object_or_404(Voucher, pk=voucher_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        shopping_bag[voucher_id] = quantity
        messages.success(
            request,
            f'Updated {voucher.title} quantity to {shopping_bag[voucher_id]}')
    else:
        shopping_bag.pop(voucher_id)
        messages.success(
            request, f'Removed {voucher.title} from your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shopping_bag'))


# view to remove vouchers from the shopping bag
def remove_from_shopping_bag(request, voucher_id):
    """ Remove the specified voucher from the shopping bag """

    try:
        voucher = get_object_or_404(Voucher, pk=voucher_id)
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag.pop(voucher_id)
        messages.success(
            request, f'Removed {voucher.title} from your shopping bag')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
