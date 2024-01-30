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
    """ A view to allow a superuser to add a new voucher """
    form = VoucherForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vouchers')

    return render(request, 'flights/add_voucher.html', {'form': form})


def edit_voucher(request, id):
    """ A view to allow a superuser to edit a voucher """
    voucher = get_object_or_404(Voucher, id=id)
    if not request.user.is_superuser:
        return redirect('vouchers')
    form = VoucherForm(
        request.POST or None, request.FILES or None, instance=voucher)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vouchers')
    context = {
        'form': form,
        'voucher': voucher,
    }

    return render(request, 'flights/edit_voucher.html', context)


def delete_voucher(request, id):
    """ A view to allow a superuser to delete a voucher """
    voucher = get_object_or_404(Voucher, id=id)
    if not request.user.is_superuser:
        return redirect('vouchers')
    voucher.delete()
    return redirect('vouchers')