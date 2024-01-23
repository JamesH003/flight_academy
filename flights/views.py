from django.shortcuts import render
from .models import Voucher

# Create your views here.

def all_vouchers(request):
    """ A view to show all vouchers """

    vouchers = Voucher.objects.all()

    context = {
        'vouchers': vouchers,
    }
    
    return render(request, 'flights/vouchers.html', context)