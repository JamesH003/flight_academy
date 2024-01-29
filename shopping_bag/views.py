from django.shortcuts import render, redirect

# Create your views here.

def view_shopping_bag(request):
    """ A view that renders the shopping bag contents page """
    
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, voucher_id):
    """ Add a quantity of the specified voucher to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if voucher_id in list(shopping_bag.keys()):
        shopping_bag[voucher_id] += quantity
    else:
        shopping_bag[voucher_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(redirect_url)