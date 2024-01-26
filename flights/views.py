from django.shortcuts import render, get_object_or_404, redirect
from .models import Voucher, Aircraft
from .forms import VoucherForm

# Create your views here.

def all_vouchers(request):
    """ A view to show all vouchers """

    vouchers = Voucher.objects.all()

    context = {
        'vouchers': vouchers,
    }
    
    return render(request, 'flights/vouchers.html', context)


def voucher_detail(request, voucher_id):
    """ A view to show individual voucher details """

    voucher = get_object_or_404(Voucher, pk=voucher_id)

    context = {
        'voucher': voucher,
    }
    
    return render(request, 'flights/voucher_detail.html', context)


def add_voucher(request):
    form = VoucherForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vouchers')

    return render(request, 'flights/add_voucher.html', {'form': form})
